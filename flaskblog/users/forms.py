from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    """A class to represent the form that users will use to register to the forum. It includes fields for `username`, `email`, `password`, and `confirm_password`. 

    - `username`: This creates a text field for the user's `username`, with validators ensuring it is not empty and is between 2 and 20 characters long.

    - `email` : This creates a text field for the user's `email`, with validators ensuring it is not empty and is a valid email address.

    - `password`: This creates a password field for the user's password, with a validator ensuring it is not empty.

    - `confirm_password`: This creates a password field for the user to confirm their password, with validators ensuring it is not empty and matches the entered password.

    - `submit`: This creates a submit button for the form.

    - `validate_username(self, username)`: This method validates the `username` field, checking if a user with the same `username` already exists in the database.

    - `validate_email(self, email)`: This method validates the `email` field, checking if a user with the same `email` already exists in the database.
    """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """This method validates the `username` field, checking if a user with the same `username` already exists in the database.

        If a user with the same `username` already exists, a `ValidationError` is raised.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """This method validates the `email` field, checking if a user with the same `email` already exists in the database.

        If a user with the same `email` already exists, a `ValidationError` is raised.
        """
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    """A class to represent the form that users will use to login to the forum. It includes fields for `email`, `password`, and `remember`. 

    The class defines four fields:

    -   `email`: A text field for the user's email, with validators ensuring it is not empty and is a valid email address.
    -   `password`: A password field for the user's password, with a validator ensuring it is not empty.
    -   `remember`: A boolean field for the user to choose whether to remember their login credentials.
    -   `submit`: A submit button for the form.

    """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    # TODO: Add change password choice
    """A class to represent the form that users will use to update their account for the forum. It includes fields for `username`, `email`, `password`, and `confirm_password`. 

    Fields:
    
    - `username`: This creates a text field for the user's `username`, with validators ensuring it is not empty and is between 2 and 20 characters long.

    - `email` : This creates a text field for the user's `email`, with validators ensuring it is not empty and is a valid email address.

    - `picture`: This lets users choose a profile picture for their account. Extensions allowed: png, jpeg, jpg.

    - `password`: This creates a password field for the user's password, with a validator ensuring it is not empty.

    - `confirm_password`: This creates a password field for the user to confirm their password, with validators ensuring it is not empty and matches the entered password.

    - `submit`: This creates a submit button for the form.

    - `validate_username(self, username)`: This method validates the `username` field, checking if a user with the same `username` already exists in the database.

    - `validate_email(self, email)`: This method validates the `email` field, checking if a user with the same `email` already exists in the database."""
        
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators= [FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        """This method validates the `username` field, checking if a user with the same `username` already exists in the database.

        If a user with the same `username` already exists, a `ValidationError` is raised.
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """This method validates the `email` field, checking if a user with the same `email` already exists in the database.

        If a user with the same `email` already exists, a `ValidationError` is raised.
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
            

class RequestResetForm(FlaskForm):
    """
    The RequestResetForm class creates a form that allows users to request a password reset. 

    Fields:

    * `email`: A text field for the user's email, with validators ensuring it is not empty and is a valid email address.
    * `submit`: A submit button for the form.
    * `validate_email(self, email)`: This method checks if the provided email address is associated with an existing user account. If not, it raises a validation error with a message prompting the user to register first.
    """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        """This method validates the `email` field, checking if a user with the same `email` already exists in the database.

        If a user with the same `email` already exists, a `ValidationError` is raised.
        """
        email = User.query.filter_by(email=email.data).first()
        if email is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    """
    The ResetPasswordForm class creates a form for resetting a password, with fields for entering a new password and confirming it.

    Fields:

    * `password`: Creates a password field that requires input (due to `DataRequired()` validator).
    * `confirm_password`: Creates a password field that requires input (due to `DataRequired()` validator) and must match the `password` field (due to `EqualTo('password')` validator).
    * `submit`: Creates a submit button for the form.

    Note that this class does not have any explicit methods, only field definitions. The validation logic is handled by the validators attached to each field."""
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Passowrd')
    