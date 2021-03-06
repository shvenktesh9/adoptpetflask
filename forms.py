from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    full_name=StringField('name',validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm', validators=[EqualTo('password'), InputRequired()])
    submit = SubmitField('Sign Up')

    
class EditPetForm(FlaskForm):
    name = StringField("Pet's Name", validators = [InputRequired()])
    age = StringField("Pet's Age", validators = [InputRequired()])
    bio = StringField("Pet's Bio", validators = [InputRequired()])
    submit = SubmitField("Edit Pet")
