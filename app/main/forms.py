from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField,
    StringField,
    SubmitField,
)
from wtforms.validators import InputRequired, Length

from app.models import Habit

class HabitForm(FlaskForm):
    description = StringField('Title', validators=[InputRequired(), 
                                                   Length(1, 240)])
    complete = BooleanField('Completed')
    submit = SubmitField('Add habit')