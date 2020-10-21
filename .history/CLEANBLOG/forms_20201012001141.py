from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max = 20)])