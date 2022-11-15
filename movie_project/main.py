from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from model import db, Movie
from form import EditForm

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


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    found_movie = Movie.query.get(movie_id)
    form = EditForm()

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


if __name__ == '__main__':
    app.run(debug=True)
