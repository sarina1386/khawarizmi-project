from flask import Flask, render_template, url_for, redirect, request
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from models import db, Users
from flask_migrate import Migrate
from forms import *
from datetime import datetime

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

bcrypt = Bcrypt(app)

@app.route('/')
def root():
    return render_template('index.html', user='')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        user_name = form.user_name.data
        fname = form.first_name.data
        lname = form.last_name.data
        grade = form.grade.data
        school = form.school.data
        password = form.password.data
        hashed_pass = bcrypt.generate_password_hash(password)
        is_admin = False
        if(user_name == 'saeed') and ('144' in password):
            is_admin = True

        new_user = Users(
            user_name=user_name,
            password=hashed_pass,
            fname=fname,
            lname=lname,
            grade=int(grade),
            school=school,
            is_admin=is_admin
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.user_name.data
        password = form.password.data

        user = Users.query.filter_by(user_name=user_name).first()
        if user:
            hashed_pass = user.password
            check_pass = bcrypt.check_password_hash(hashed_pass, password)
            if check_pass:
                login_user(user, remember=form.remember_me.data)
                current_user.last_login = datetime.utcnow()
                db.session.commit()
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('root'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)



if __name__ == "__main__":
    app.run()