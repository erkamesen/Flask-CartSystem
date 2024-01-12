from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'courses.db')

# Uygulama Eklentileri
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.init_app(app)

from app.admin.views import MyAdminIndexView
admin = Admin(app, name='Admin', index_view=MyAdminIndexView(), template_mode='bootstrap3')

from app.models import Course, Category, User, Cart, CartItem
from app.admin import CourseModelView, CategoryModelView, UserModelView
from flask_admin.contrib.sqla import ModelView
admin.add_view(UserModelView(User, db.session))
admin.add_view(CourseModelView(Course, db.session))
admin.add_view(CategoryModelView(Category, db.session))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    from app.home import home_bp
    from app.user import user_bp
    from app.product import course_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(course_bp)
    
    return app