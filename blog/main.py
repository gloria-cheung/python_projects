from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/blog')
def blog():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def post(id):
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    single_post = None
    for post in posts:
        if post["id"] == id:
            single_post = post
    return render_template("post.html", post=single_post)


if __name__ == "__main__":
    app.run(debug=True)
