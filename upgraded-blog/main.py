from flask import Flask, render_template, request
import requests
from smtplib import SMTP
from dotenv import load_dotenv
import os
app = Flask(__name__)


@app.route("/")
def index():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def post(id):
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    found_post = None
    for post in posts:
        if post["id"] == id:
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