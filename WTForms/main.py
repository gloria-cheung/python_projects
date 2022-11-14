from flask import Flask, render_template, redirect
from forms import MyForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)