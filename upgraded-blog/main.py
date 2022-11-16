from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from smtplib import SMTP
from dotenv import load_dotenv
import os
from model import BlogPost, db
from form import CreatePostForm
from flask_ckeditor import CKEditor
import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    posts = BlogPost.query.all()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def post(id):
    posts = BlogPost.query.all()
    found_post = None
    for post in posts:
        if post.id == id:
            found_post = post
    return render_template("post.html", post=found_post)


@app.route("/new-post", methods=["GET", "POST"])
def create():
    form = CreatePostForm()
    if form.validate_on_submit():
        date = datetime.datetime.now()
        formatted_date = f"{date.strftime('%B')} {date.day}, {date.year}"

        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date=formatted_date
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")
    return render_template("make-post.html", form=form, status="create")


@app.route("/edit-post/<int:id>", methods=["GET", "POST"])
def update(id):
    found_post = BlogPost.query.get(id)
    # populate form with post data
    form = CreatePostForm(obj=found_post)

    # take all data from submitted form and update
    if form.validate_on_submit():
        found_post.title = form.title.data
        found_post.subtitle = form.subtitle.data
        found_post.author = form.author.data
        found_post.img_url = form.img_url.data
        found_post.body = form.body.data
        db.session.commit()
        return redirect(f"/post/{id}")

    return render_template("make-post.html", form=form, status="update", id=id)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = ""
    if request.method == "GET":
        message = "Contact Me"
    elif request.method == "POST":
        # send email
        load_dotenv()
        email = os.getenv("email")
        password = os.getenv("password")

        server = SMTP("smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        SMTP.sendmail(self=server, from_addr="gloriacheung812@smtp.gmail.com", to_addrs="gloriacheung812@gmail.com",
                      msg="Subject: Blog Contact Form \n\nMessage from {} at {}: \n\n{}".format(request.form["name"], request.form["email"], request.form["message"]))
        message = "Successfully sent message"

    return render_template("contact.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)