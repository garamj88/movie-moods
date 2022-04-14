from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

class MovieListForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    mood = StringField('When in the Mood for', validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired()])
    release_year = IntegerField('Release Year', validators=[DataRequired()])
    submit = SubmitField('Submit')