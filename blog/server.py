from flask import Flask
from flask import render_template
import requests
import json
import random
import datetime
app = Flask(__name__)


@app.route("/")
def home():
    random_num = random.randint(1,10)
    year = datetime.date.today().year
    return render_template("index.html", num=random_num, year=year)


@app.route("/guess/<name>")
def ageify(name):
    parsed_age_data = requests.get(f"https://api.agify.io/?name={name}").json()
    parsed_gender_data = requests.get(f"https://api.genderize.io?name={name}").json()
    return render_template("guess.html", name=name, age=parsed_age_data["age"], gender=parsed_gender_data["gender"])

if __name__ == "__main__":
    app.run(debug=True)