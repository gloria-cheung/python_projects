from flask import Flask, render_template, request, jsonify
import requests
from smtplib import SMTP
from dotenv import load_dotenv
import os
from model import BlogPost, db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
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