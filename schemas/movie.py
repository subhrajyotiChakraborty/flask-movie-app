from ma import ma
from models.movie import MovieModel


class MovieSchema(ma.SQLAlchemyAutoSchema):

    class Meta():
        model = MovieModel
        dump_only = ("id", )
        load_instance = True