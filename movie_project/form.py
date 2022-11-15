from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 eg 7.5:', validators=[DataRequired()])
    review = StringField('Your Review:', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField('Movie Title:', validators=[DataRequired()])
    submit = SubmitField('Add Movie')