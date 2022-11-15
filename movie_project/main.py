from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from model import db, Movie
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db.init_app(app)
Bootstrap(app)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
