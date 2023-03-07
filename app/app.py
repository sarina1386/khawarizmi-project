from flask import Flask, render_template, url_for, redirect, request, jsonify, abort
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Users, Contents
from forms import RegisterForm, LoginForm
from flask_bcrypt import Bcrypt
import json

# Initializing the app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.debug = True
app.config['SECRET_KEY'] = 'FarzanSchool'

# Initializing the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Initializing the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# Register page
@app.route('/register', methods=('GET', 'POST'))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        is_admin = False
        user_name = form.user_name.data
        fname = form.first_name.data
        lname = form.last_name.data
        grade = form.grade.data
        password = form.password.data
        hashed_pass = bcrypt.generate_password_hash(password)
        print(type(user_name), type(fname))
        if('saeed144' in user_name):
            is_admin = True
        activity = "{}"
        user = Users.query.filter_by(user_name=user_name).first()
        if not user:
            new_user = Users(user_name=user_name, password=hashed_pass, fname=fname,
            lname=lname, is_admin=is_admin, grade=grade, activity=activity)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return render_template('register.html', form=form)
    return render_template('register.html', form=form)

# Login page
@app.route('/login', methods=('GET', 'POST'))
def login():
    # Already logged user does not need to login page
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.user_name.data
        password = form.password.data
        user = Users.query.filter_by(user_name=form.user_name.data).first()
        print(user)
        if user:
            print('success')
            hashed_pass = user.password
            check_pass = bcrypt.check_password_hash(user.password, password)
            if check_pass:
                login_user(user, remember=form.remember_me.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            print(check_pass)
            print(hashed_pass)
        print(user)
    return render_template('login.html', form=form)

# Logout page
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Landing page
@app.route('/')
@app.route('/landing')
def landing():
    user = ''
    if current_user.is_authenticated:
        user = current_user
        return redirect(url_for('home'))
    print(user)
    return render_template('index.html', user=user)

# Home page
@app.route('/home')
@login_required
def home():
    user = current_user
    return render_template('home.html', user=user)

# Getting content info
@app.route('/get-content-info', methods=["POST"])
@login_required
def get_content_info():
    data = request.get_json()
    if(data['grade'] < 10):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

# Course page
@app.route('/course')
@login_required
def course():
    user=current_user
    user_id = request.args.get('user_id')
    grade = request.args.get('grade')
    lesson = request.args.get('lesson')
    session = request.args.get('session')
    content = Contents.query.filter(Contents.grade==grade).filter(Contents.lesson == lesson).filter(Contents.session == session).first()

    if not content:
        return redirect(url_for('home', sit=1))

    script = content.script
    video = content.video
    deaf = content.deaf
    tabs = json.loads(content.tabs_content)
    quiz = json.loads(content.quiz)

    return render_template(
        'course.html',
        user=user,
        script=script,
        video=video,
        deaf=deaf,
        tabs=tabs,
        quiz=quiz
    )

# Adding course
@app.route('/add-course', methods=["GET", "POST"])
@login_required
def add_course():
    if current_user.is_admin:
        grade = 7
        lesson = 1
        session = 1
        script = 't711.jpg'
        # https://www.aparat.com/video/video/embed/videohash/...../vt/frame
        video = 'yQbWO'
        deaf = 'LRU3i'
        quiz_dict = {
            'num': 5,
            1: ['چگونه تقسیم کنیم؟', 'q911.png', [25.2, 35, 22, 20], 2],
            2: ['مثلثات چیست؟', 'q911.png', [10, 11, 9, 8], 2],
            3: ['زاویه حاده را چگونه بیابم', 'q911.png', [1225, 1457, 1111, 890], 4],
            4: ['توان 2', 'q911.png', [0.02, 0.07, 0.08, 0.04], 3],
            5: ['لگاریتم', 'q911.png', [1, 2, 3, 4], 1],

        }
        quiz = json.dumps(quiz_dict)
        tabs_num = 3
        tabs_content_dict = {
            1: ['بخش اول', 'yQbWO', 'LRU3i', 't711.jpg'],
            2: ['بخش دوم', 'yQbWO', 'LRU3i', 't711.jpg'],
            3: ['بخش سوم', 'yQbWO', 'LRU3i', 't711.jpg']
        }
        tabs_content = json.dumps(tabs_content_dict)
        # cnt = Contents.query.get(1)
        # cnt.script = script
        # cnt.quiz = quiz
        # cnt.tabs_content = tabs_content

        # new_content = Contents(
        #     grade=grade,
        #     lesson=lesson,
        #     session=session,
        #     script=script,
        #     video=video,
        #     deaf=deaf,
        #     quiz=quiz,
        #     tabs_num=tabs_num,
        #     tabs_content=tabs_content
        # )
        try:
            # db.session.add(new_content)
            # db.session.commit()
            return 'done'
        except:
            return 'failed'
    abort(404, 'Resource not found')

# Adding course
@app.route('/submit-result', methods=["POST"])
@login_required
def submit_result():
    data = request.get_json()
    user = Users.query.get(int(data['id']))
    activities = json.loads(user.activity)
    activity = [data['content'], data['res']]
    if not activities:
        activities.append(activity)
    else:
        for act in activities:
            if act[0] == data['content']:
                act[1] = data['res']
            else:
                activities.append(activity)

    user.activity = json.dumps(activities)
    db.session.commit()
    return jsonify({'success': True})


@app.route('/lesson')
def lesson():
    return 'lesson'

# Start the app
if __name__ == '__main__':
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    app.run()