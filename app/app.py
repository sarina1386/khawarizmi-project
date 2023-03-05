from flask import Flask, render_template, url_for
from flask_login import LoginManager, login_user, current_user, logout_user
from models import db, Users
from flask_migrate import Migrate

app = Flask(__name__, template_folder='templates', static_folder='static')

app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
migrate = Migrate(app, db)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == "__main__":
    app.run()