import os
import secrets
from typing import Any
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture: Any) -> str:
    """
    Saves a resized picture to the server.

    Args:
        form_picture (Any): The uploaded picture file.

    Returns:
        str: The filename of the saved picture.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user: Any) -> None:
    """
    Sends a password reset email to the user.

    Args:
        user (Any): The user object for which the email is being sent.
    """
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demomailtrap.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, simply ignore this email and no changes will be made.
'''
    mail.send(msg)
