from flask import Flask, render_template, url_for
from flask_login import LoginManager, login_user, current_user, logout_user
from models import db, Users
from flask_migrate import Migrate
from forms import *

app = Flask(__name__, template_folder='templates', static_folder='static')

app.debug = True
app.config['SECRET_KEY'] = 'sarina_sonia'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')





if __name__ == "__main__":
    app.run()