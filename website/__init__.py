from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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

    


    return app