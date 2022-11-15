from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from model import db, Movie
from form import EditForm, AddForm
from dotenv import load_dotenv
import os
import requests


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db.init_app(app)
Bootstrap(app)

# api key to fetch movie data
load_dotenv()
api_key = os.getenv("API_KEY")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    found_movie = Movie.query.get(movie_id)
    form = EditForm()

    if not found_movie:
        # get data from API and create new movie (with missing rating, ranking, review)
        data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}").json()
        new_movie = Movie(
            title=data["title"],
            year=int(data["release_date"][:4]),
            description=data["overview"],
            img_url=f"https://image.tmdb.org/t/p/original{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()

        # find that movie in db and send it back to edit route to update the missing info
        found_movie = Movie.query.filter_by(title=data["title"]).first()

    # checks if POST req and validates
    if form.validate_on_submit():
        found_movie.rating = form.rating.data
        found_movie.review = form.review.data
        db.session.commit()
        return redirect("/")

    return render_template("edit.html", movie=found_movie, form=form)


@app.route("/delete/<int:movie_id>", methods=["POST"])
def delete(movie_id):
    found_movie = Movie.query.get(movie_id)
    db.session.delete(found_movie)
    db.session.commit()
    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={form.title.data}").json()
        return render_template("select.html", movies=data["results"])
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
