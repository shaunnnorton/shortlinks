from multiprocessing import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
# APPSETUP
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)
# DBSETUP
db = SQLAlchemy(app)
# LOGINSETUP
# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# login_manager.init_app(app)



from src.main import main_routes as main_routes
app.register_blueprint(main_routes)



with app.app_context():
    db.create_all()