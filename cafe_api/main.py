from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def obj_to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    # get all cafes and see how many available, then choose random index and return that cafe
    cafes = db.session.query(Cafe).all()
    rand_idx = random.randint(0, len(cafes))
    cafe = Cafe.query.get(rand_idx)
    return jsonify(cafe=cafe.obj_to_dict())


@app.route("/all")
def all():
    cafes = Cafe.query.all()
    result = [cafe.obj_to_dict() for cafe in cafes]
    return jsonify(cafes=result)


@app.route("/search")
def search():
    args = request.args
    location = args.get('loc')
    cafes = Cafe.query.filter_by(location=location).all()
    if len(cafes) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    else:
        result = [cafe.obj_to_dict() for cafe in cafes]
        return jsonify(cafes=result)

## HTTP POST - Create Record
@app.route("/all", methods=["POST"])
def create():
    cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=bool(request.form["has_toilet"]),
        has_wifi=bool(request.form["has_wifi"]),
        has_sockets=bool(request.form["has_sockets"]),
        can_take_calls=bool(request.form["can_take_calls"]),
        coffee_price=request.form["coffee_price"]
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe"})


## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
