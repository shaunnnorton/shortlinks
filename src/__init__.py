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
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from src.models import Admin
@login_manager.user_loader
def load_admin(admin_id):
    return Admin.query.get(admin_id)



bcrypt = Bcrypt(app)

# ROUTES SETUP
from src.auth.routes import auth as auth_routes
app.register_blueprint(auth_routes)

from src.main import main_routes as main_routes
app.register_blueprint(main_routes)



# CREATING DB
with app.app_context():
    db.create_all()


# CREATING ADMIN ACCOUNT
try:
    admin_password = bcrypt.generate_password_hash(os.getenv("ADMIN_PASSWORD")).decode("utf-8")
    admin = Admin(
        username=os.getenv("ADMIN_USERNAME"),
        password=admin_password
        )
    db.session.add(admin)
    db.session.commit()
    print(f'Admin Account Created {admin}')
except:
    db.session.rollback()
    existing_admin = Admin.query.filter_by(username=os.getenv("ADMIN_USERNAME")).first()
    print(f"Admin already exists {existing_admin}")