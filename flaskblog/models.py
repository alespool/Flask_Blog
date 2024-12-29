from datetime import datetime
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin
from typing import Optional


@login_manager.user_loader
def load_user(user_id: int) -> Optional["User"]:
    """
    Loads a user by their ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        Optional[User]: The user object if found, otherwise None.
    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    Represents a user in the system.

    Attributes:
        id (int): The user's unique identifier.
        username (str): The user's username.
        email (str): The user's email address.
        image_file (str): The filename of the user's profile image.
        password (str): The user's hashed password.
        posts (list[Post]): The list of posts created by the user.
    """
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(20), unique=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    image_file: str = db.Column(db.String(20), nullable=False, default='brainsurgeon.jpg')
    password: str = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self) -> str:
        """
        Generates a token for resetting the user's password.

        Returns:
            str: A serialized token containing the user's ID.
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token: str) -> Optional["User"]:
        """
        Verifies a reset token and returns the associated user.

        Args:
            token (str): The reset token to verify.

        Returns:
            Optional[User]: The user associated with the token if valid, otherwise None.
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except Exception:
            return None
        return User.query.get(user_id)

    def __repr__(self) -> str:
        """
        Returns a string representation of the user.

        Returns:
            str: A string with the user's details.
        """
        return f"User('{self.username}'), User('{self.email}'), User('{self.image_file}')"


class Post(db.Model):
    """
    Represents a blog post in the system.

    Attributes:
        id (int): The post's unique identifier.
        title (str): The title of the post.
        date_posted (datetime): The date and time the post was created.
        content (str): The content of the post.
        user_id (int): The ID of the user who created the post.
    """
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(100), nullable=False)
    date_posted: datetime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content: str = db.Column(db.Text, nullable=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_announcement: bool = db.Column(db.Boolean, default=False)

    def excerpt(self, length=200):
        # Return the first 'length' characters of the post content
        return self.content[:length] + "..." if len(self.content) > length else self.content

    def __repr__(self) -> str:
        """
        Returns a string representation of the post.

        Returns:
            str: A string with the post's title and date posted.
        """
        return f"Post('{self.title}', '{self.date_posted}')"
