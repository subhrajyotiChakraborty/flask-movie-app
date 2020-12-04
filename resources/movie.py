import os
from flask_restful import Resource
from flask import request
import requests

from schemas.movie import MovieSchema
from models.movie import MovieModel

movie_schema = MovieSchema()
movie_list_schema = MovieSchema(many=True)


class Movie(Resource):
    @classmethod
    def post(cls):
        movie_json = request.get_json()
        movie = movie_schema.load(movie_json)

        if MovieModel.find_by_imdbID(movie.imdbID):
            return {"message": f"Movie with this {movie.imdbID} is already exists"}, 400

        try:
            movie.isFav = True
            movie.save_to_db()
        except:
            return {"message": "Error while saving your favorite movie in to DB"}, 500

        return movie_schema.dump(movie), 201


class GetMovies(Resource):
    @classmethod
    def get(cls, movieName: str):
        page_count = request.args.get("page") if request.args.get("page") else "1"

        if int(int(page_count)) < 1:
            page_count = "1"

        try:
            r = requests.get(f"http://www.omdbapi.com/?apikey={os.environ.get('API_KEY')}&s=/{movieName}&page={page_count}")
        except:
            return {"message": "Error occurred while fetching movies data"}, 500

        return r.json(), 200


class GetMovieDetails(Resource):
    @classmethod
    def get(cls, imdbID: str):
        try:
            print(f"http://www.omdbapi.com/?i={imdbID}&apikey={os.environ.get('API_KEY')}")
            response = requests.get(f"http://www.omdbapi.com/?i={imdbID}&apikey={os.environ.get('API_KEY')}")
        except:
            return {"message": "Error occurred while fetching movie details"}, 500

        return response.json(), 200


class DeleteMovie(Resource):
    @classmethod
    def delete(cls, imdbID: str):
        movie = MovieModel.find_by_imdbID(imdbID)

        if movie:
            movie.delete_from_db()
            return {"message": "Movie deleted successfully"}, 200

        return {"message": f"Error!!, movie with {imdbID} imdbID was not found"}, 404


class MovieList(Resource):
    @classmethod
    def get(cls):
        return {"movies": movie_list_schema.dump(MovieModel.find_all())}, 200
