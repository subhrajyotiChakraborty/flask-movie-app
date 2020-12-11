from typing import List

from db import db


class MovieModel(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Poster = db.Column(db.String, nullable=False)
    Type = db.Column(db.String(10))
    Year = db.Column(db.String(5), nullable=False)
    imdbID = db.Column(db.String(20), nullable=False, unique=True)
    isFav = db.Column(db.Boolean)

    @classmethod
    def find_by_imdbID(cls, imdbID: str) -> "MovieModel":
        return cls.query.filter_by(imdbID=imdbID).first()

    @classmethod
    def find_all(cls) -> List["MovieModel"]:
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
