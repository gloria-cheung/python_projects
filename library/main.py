from flask import Flask, render_template, request, redirect
from model import db, Book
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # create new book and save to db
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()

        return redirect("/")
    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    found_book = Book.query.get(book_id)

    if request.method == "POST":
        # update book rating and save to db
        found_book.rating = request.form["rating"]
        db.session.commit()

        return redirect("/")
    return render_template("edit.html", book=found_book)


@app.route("/delete/<int:book_id>", methods=["POST"])
def delete(book_id):
    found_book = Book.query.get(book_id)
    db.session.delete(found_book)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
