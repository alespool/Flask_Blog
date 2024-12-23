from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_pagedown import PageDown

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

# from authlib.integrations.flask_client import OAuth

# OAuth Configurations
# app.config['GOOGLE_CLIENT_ID'] = os.environ.get('GOOGLE_CLIENT_ID')
# app.config['GOOGLE_CLIENT_SECRET'] = os.environ.get('GOOGLE_CLIENT_SECRET')

# oauth = OAuth(app)
# google = oauth.register(
#     name='google',
#     client_id=app.config['GOOGLE_CLIENT_ID'],
#     client_secret=app.config['GOOGLE_CLIENT_SECRET'],
#     access_token_url='https://oauth2.googleapis.com/token',
#     authorize_url='https://accounts.google.com/o/oauth2/auth',
#     api_base_url='https://www.googleapis.com/oauth2/v1/',
#     client_kwargs={
#         'scope': 'email profile',
#     },
# )


def create_app(config_class=Config):
    
    app = Flask(__name__)
    pagedown = PageDown(app)
    
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app