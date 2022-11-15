from flask import Flask, render_template, request, redirect

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_dict = {}
        for item in request.form.items():
            if item[0] == "rating":
                book_dict[item[0]] = int(item[1])
            else:
                book_dict[item[0]] = item[1]
        all_books.append(book_dict)

        return redirect("/")
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
    