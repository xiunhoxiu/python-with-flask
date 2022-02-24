from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()  # object to add/create new user to the db
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asaldlfjlk alfakjie aklsjfl'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # sqlite or SQL db is located/stored at f'sqlite:///{DB_NAME}' using flask within the website folder
    db.init_app(app)  # using the Flask app with the db.

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Note

    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        # telling flask how to load a user
        # .get() - look for the primary key
    return app


def create_database(app):
    # Check if the data exists via path from OS (operational system)
    # if not db will be created
    # passing app to tell SQLAlchemey which app the db will be created for.
    # the app also have the sqlalchemey db URI that tells where to create the db.
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
