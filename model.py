from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class movies(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, unique =True, nullable = False)
    rating = db.Column(db.Integer)
    poster = db.Column(db.String, nullable = False)
    genre = db.relationship("genre", secondary="movie_g")
    venues = db.relationship("venues",secondary="movie_venue")

class venues(db.Model):
    __tablename__ = "venues"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique =True, nullable = False)
    location = db.Column(db.String, nullable = False)

class genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, unique = True)
    type = db.Column(db.String, unique =True, nullable = False)

class movie_g(db.Model):
    __tablename__ = "movie_g"
    m_id = db.Column(db.Integer,db.ForeignKey("movies.id"), primary_key = True, nullable = False)
    g_id = db.Column(db.Integer,db.ForeignKey("genre.id"), primary_key = True, nullable = False)

class movie_venue(db.Model):
    __tablename__ = "movie_venue"
    m_id = db.Column(db.Integer,db.ForeignKey("movies.id"), primary_key = True, nullable = False)
    v_id = db.Column(db.Integer,db.ForeignKey("venues.id"), primary_key = True, nullable = False)


class users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, unique = True)
    username = db.Column(db.String, unique =True, nullable = False)
    email = db.Column(db.String, unique =True, nullable = False)
    password = db.Column(db.String, unique =True, nullable = False)
