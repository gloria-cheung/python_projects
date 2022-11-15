from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location = URLField('Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening Time (eg:8AM)', validators=[DataRequired()])
    close = StringField('Closing Time (eg: 8PM)', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', validators=[DataRequired()], choices=[("✘", "✘"), ("☕", "☕"), ("☕☕", "☕☕"), ("☕☕☕", "☕☕☕"), ("☕☕☕☕", "☕☕☕☕")])
    wifi = SelectField('Wifi Rating', validators=[DataRequired()], choices=[("✘", "✘"), ("💪", "💪"), ("💪💪", "💪💪"), ("💪💪💪", "💪💪💪"), ("💪💪💪💪", "💪💪💪💪")])
    power = SelectField('Power Rating', validators=[DataRequired()], choices=[("✘", "✘"), ("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌"), ("🔌🔌🔌🔌", "🔌🔌🔌🔌")])
    submit = SubmitField("Submit")