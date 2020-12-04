import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
from marshmallow import ValidationError

from db import db
from ma import ma
from resources.movie import Movie, DeleteMovie, MovieList, GetMovies, GetMovieDetails

app = Flask(__name__)
CORS(app)

# for dev
# load_dotenv(".env", verbose=True)
# app.config.from_object("default_config")
# app.config.from_envvar("APPLICATION_SETTINGS")

api = Api(app)

# for production
app.config.from_object("config")
app.config.from_envvar("APPLICATION_SETTINGS")


# for dev
# @app.before_first_request
# def create_tables():
#     db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


api.add_resource(GetMovies, "/movies/<string:movieName>")
api.add_resource(Movie, "/movie")
api.add_resource(GetMovieDetails, "/movie/<string:imdbID>")
api.add_resource(DeleteMovie, "/movie/<string:imdbID>")
api.add_resource(MovieList, "/favorites")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True)
