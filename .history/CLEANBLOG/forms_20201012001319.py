from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max = 20)])
    email = StringField('Email', validators=[DataRequired(), Email])
    password = PasswordField('')