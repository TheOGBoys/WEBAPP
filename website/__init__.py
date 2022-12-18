from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#AIL INI 17.12.22
db = SQLAlchemy()
DB_NAME = "database.db"
#AIL END 17.12.22

def create_app():
    app = Flask(__name__)

    #AIL INI 17.12.22
    app.config['SECRET_KEY'] = 'The Boys' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth  import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth,  url_prefix='/')

    from .models import User, Note

    #AIL END 17.12.22
    
    return app
    
#AIL INI 17.12.22
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
#AIL END 17.12.22