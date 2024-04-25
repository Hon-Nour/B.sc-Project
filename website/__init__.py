from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore
from os import path
from flask_login import LoginManager # type: ignore

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3307/hall_allocation'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Users, Role, Biodata, Activitycategory, Occurrence, semester, Session, Activity, Time

    with app.app_context():
        db.create_all()
        print('Created Database!')

    return app
