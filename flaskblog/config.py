import os

class Config:
    """
    Configuration class for the Flask application.

    Attributes:
        SECRET_KEY (str): The secret key for securely signing session cookies and other secrets.
        SQLALCHEMY_DATABASE_URI (str): The database URI for SQLAlchemy.
        MAIL_SERVER (str): The mail server host.
        MAIL_PORT (int): The port used by the mail server.
        MAIL_USE_TLS (bool): Whether to use TLS (Transport Layer Security) for email.
        MAIL_USE_SSL (bool): Whether to use SSL (Secure Sockets Layer) for email.
        MAIL_USERNAME (str): The username for the mail server authentication.
        MAIL_PASSWORD (str): The password for the mail server authentication.
    """

    SECRET_KEY: str | None = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI: str | None = os.environ.get('SQLALCHEMY_DATABASE_URI')

    MAIL_SERVER: str = 'live.smtp.mailtrap.io'
    MAIL_PORT: int = 587
    MAIL_USE_TLS: bool = True
    MAIL_USE_SSL: bool = False
    MAIL_USERNAME: str | None = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD: str | None = os.environ.get('MAIL_PASSWORD')
