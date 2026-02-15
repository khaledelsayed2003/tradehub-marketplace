from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=2, max=50), DataRequired()])
    email_address = StringField(label='Email', validators=[Length(max=100), Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password_confirmation = PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Sign up')
    
    