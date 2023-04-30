from flask import Flask, render_template, url_for, redirect, request, abort, jsonify, session
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from models import db, Users, Lessons, Quiz
from flask_migrate import Migrate
from forms import *
from datetime import datetime
import json

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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

@app.route('/admin/add-lesson', methods=['GET', 'POST'])
@login_required
def add_lesson():
    if not current_user.is_admin:
        abort(403, 'You have no premission')
    form = AddLessonForm()
    if form.validate_on_submit():
        lesson_name = form.lesson_name.data
        grade = form.grade.data
        image = form.image.data
        sections_num = form.sections_num.data
        sections_info = form.sections_info.data

        sections_info_dict = {}
        for i in range(sections_num):
            sections_info_dict[i+1] =  ''

        if not image:
            image = 'lesson-defualt'
        sections_info_list = sections_info.split('-')
        
        if len(sections_info_list) <= sections_num:
            for i in range(len(sections_info_list)):
               sections_info_dict[i+1] =  sections_info_list[i]
        else:
            for i in range(sections_num):
               sections_info_dict[i+1] =  sections_info_list[i]
        
        new_lesson = Lessons(
            grade=grade,
            name=lesson_name,
            image=image,
            sections_num=sections_num,
            sections_intro = json.dumps(sections_info_dict)
        )
        db.session.add(new_lesson)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add-lesson.html', user=current_user, form=form)

@app.route('/admin/add-quiz', methods=['GET', 'POST'])
@login_required
def add_quiz():
    if not current_user.is_admin:
        abort(403, 'You have no premission')
    
    form = AddQuizForm()
    if form.validate_on_submit():
        lesson_name = form.lesson_name.data
        grade = form.grade.data
        lesson = Lessons.query.filter(Lessons.name==lesson_name).filter(Lessons.grade==grade).first()
        lesson_id = lesson.lid
        if lesson_name == 'ریاضی':
            lesson_type = 1
        elif lesson_name == 'علوم':
            lesson_type = 2  
        elif lesson_name == 'ادبیات':
            lesson_type = 3  
        session = form.session.data
        questions = [
            form.q1.data, form.q2.data, form.q3.data,
            form.q4.data, form.q5.data, form.q6.data,
            form.q7.data, form.q8.data, form.q9.data
        ]
        answers = [
            form.a1.data, form.a2.data, form.a3.data,
            form.a4.data, form.a5.data, form.a6.data,
            form.a7.data, form.a8.data, form.a9.data
        ]
        time = form.time.data
        
        new_quiz = Quiz(
            grade=grade,
            lesson_id=lesson_id,
            lesson=lesson_type,
            session=session,
            questions=json.dumps(questions),
            answers=json.dumps(answers),
            time=time
        )
        db.session.add(new_quiz)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('add-quiz.html', user=current_user, form=form)

@app.route('/api/get-lessons', methods=['POST'])
@login_required
def get_lesson():
    data = request.get_json()
    lessons = Lessons.query.filter_by(grade=int(data['grade'])).all()
    lessons_detail = []
    for lesson in lessons:
        info = {
            'name': lesson.name,
            'image': lesson.image,
            'sections_num': lesson.sections_num,
            'sections_intro': json.loads(lesson.sections_intro)
        }
        lessons_detail.append(info)
    return jsonify({
        'status': 'ok',
        'data': lessons_detail
    })

@app.route('/game', methods=['GET', 'POST'])
@login_required
def game():
    data = ''
    if request.method == 'POST':
        data = request.get_json()
        session['selectedGame'] = data
        return jsonify({'status': 'ok'})
    else:
        data = session.get('selectedGame')

        if not data:
            return redirect(url_for('home'))
        
        grade = int(data['grade'])
        lesson = int(data['lesson'])
        level = int(data['session'])

        quiz_id = 0
        has_quiz = False
        questions = []
        answers = []
        time = 0
        is_seen = False
        star = 0
        quiz = Quiz.query.filter_by(grade=grade).filter_by(lesson=lesson).filter_by(session=level).first()
        if quiz:
            quiz_id=quiz.qid
            has_quiz = True
            questions = json.loads(quiz.questions)
            answers = json.loads(quiz.answers)
            time = quiz.time
            seen_levels = json.loads(current_user.seen_level)
            if seen_levels:
                for game in seen_levels:
                    if (game[0] == grade) and (game[1] == lesson) and (game[2] == level):
                        is_seen = True
                        star = game[3]

        return render_template(
            'game.html',
            user=current_user,
            has_quiz=has_quiz,
            questions=questions,
            answers=answers,
            time=time,
            quiz_id=quiz_id,
            is_seen=is_seen,
            star=star
        )

@app.route('/api/get-result', methods=['POST'])
@login_required
def get_result():
    data = request.get_json()
    star = int(data['star'])

    quiz = Quiz.query.get(int(data['qid']))
    grade = quiz.grade
    lesson = quiz.lesson
    level = quiz.session
    update_score = False
    seen_levels = json.loads(current_user.seen_level)
    game_played = len(seen_levels)
    if seen_levels:
        for game in seen_levels:
            if (game[0] == grade) and (game[1] == lesson) and (game[2] == level):
                if game[3] == star:
                    update_score = False
                else:
                    update_score = False
                    if game[3] < star:
                        current_user.score = current_user.score + (star - game[3])
                    else:
                        current_user.score = current_user.score - (game[3] - star)
                    game[3] = star
            else:
                game_played -= 1
        if game_played < 1:
            update_score = True
            seen_levels.append([grade, lesson ,level, star])
    else:
        update_score = True
        seen_levels.append([grade, lesson ,level, star])

    current_user.seen_level = json.dumps(seen_levels)
    if update_score:
        current_user.score += star

    db.session.commit()
    return jsonify({'status': 'ok'})

@app.route('/my-profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = current_user
    form = UpdateUserForm()
    if form.validate_on_submit():
        update_db = False
        user_name = form.user_name.data
        if user_name:
            update_db = True
            user.user_name = user_name
        fname = form.first_name.data
        if fname:
            update_db = True
            user.fname = fname
        lname = form.last_name.data
        if lname:
            update_db = True
            user.lname = lname
        grade = form.grade.data
        if grade:
            update_db = True
            user.grade = grade
        school = form.school.data
        if school:
            update_db = True
            user.school = school
        password = form.password.data
        if password:
            update_db = True
            hashed_pass = bcrypt.generate_password_hash(password)
            user.password = hashed_pass
        
        if update_db:
            db.session.commit()
        
        return redirect(url_for('profile'))

    return render_template(
        'profile.html',
        user=user,
        form=form
    )

@app.route('/stars')
def stars():
    users = Users.query.order_by(Users.score.desc()).all()
    return render_template(
        'stars.html',
        user=current_user,
        users=users
    )

@app.route('/events')
def events():
    return render_template('index.html')

@app.route('/textbooks')
def textbooks():
    return render_template('index.html')

@app.route('/about-us')
def about():
    return render_template('about-us.html')

@app.route('/contact-us')
def contact():
    return render_template('contact-us.html')

if __name__ == "__main__":
    app.run()
