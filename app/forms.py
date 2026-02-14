from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address = StringField(label='email')
    password = PasswordField(label='password')
    password_confirmation = PasswordField(label='confirm_password')
    submit = SubmitField(label='submit')
    
    