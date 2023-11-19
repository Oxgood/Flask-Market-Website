from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms import validators
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist please try a different username')

    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exist! please try a different Email Address')

    username = StringField(label='Username', validators=[validators.Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email', validators=[validators.Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[validators.Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[validators.EqualTo('password1', message='Must be equal to password')])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')