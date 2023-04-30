from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    user_name = StringField(
        'نام کاربری', 
        validators=[InputRequired(message='نام کاربری نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'نام کاربری'}
    )
    first_name = StringField(
        'نام', 
        validators=[InputRequired(message='نام نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'نام'}
    )
    last_name = StringField(
        'نام خانوادگی', 
        validators=[InputRequired(message='نام خانوادگی نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'نام خانوادگی'}
    )
    grade = IntegerField(
        'پایه تحصیلی',  
        render_kw={'placeholder': 'پایه تحصیلی'}
    )
    school = StringField(
        'نام مدرسه',  
        render_kw={'placeholder': 'نام مدرسه'}
    )
    password = PasswordField(
        'رمز ورود',  
        validators=[InputRequired(message='رمز ورود نمی تواند خالی باشد'), Length(8, 12, message='رمز عبورد باید بیشتر از 8 و کمتر از 12 کاراکتر باشد')], 
        render_kw={'placeholder': 'رمز ورود'}
    )
    re_password = PasswordField(
        'تکرار رمز ورود',  
        validators=[InputRequired(message='رمز ورود نمی تواند خالی باشد'), EqualTo('password', message='رمز ورود با تکرار رمز ورود یکسان نیست')], 
        render_kw={'placeholder': 'تکرار رمز ورود'}
    )
    submit = SubmitField('ثبت نام')


class LoginForm(FlaskForm):
    user_name = StringField(
        'نام کاربری', 
        validators=[InputRequired(message='نام کاربری نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'نام کاربری'}
    )
    password = PasswordField(
        'رمز ورود',  
        validators=[InputRequired(message='رمز ورود نمی تواند خالی باشد'), Length(8, 12, message='رمز عبورد باید بیشتر از 8 و کمتر از 12 کاراکتر باشد')], 
        render_kw={'placeholder': 'رمز ورود'}
    )
    remember_me = BooleanField('مرا بخاطر بسپار')
    submit = SubmitField('ورود')

class AddLessonForm(FlaskForm):
    lesson_name = StringField(
        'نام درس', 
        validators=[InputRequired(message='نام درس نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'نام درس'}
    )
    grade = IntegerField(
        'پایه تحصیلی درس',  
        validators=[InputRequired(message='پایه تحصیلی درس نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'پایه تحصیلی درس'}
    )
    image = StringField(
        'تصویر درس',  
        render_kw={'placeholder': 'تصویر درس (مانند: riazi7)'}
    )
    sections_num = IntegerField(
        'تعداد فصول',  
        validators=[InputRequired(message=' تعداد فصول درس نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'تعداد فصول'}
    )
    sections_info = TextAreaField(
        'عنوان هر فصل', 
        validators=[InputRequired(message='عنوان هر فصل')], 
        render_kw={'placeholder': 'عنوان هرفصل ( مقادیر را با - جدا کنید)'}
    )
    submit = SubmitField('ثبت و اضافه کردن درس')

class AddQuizForm(FlaskForm):
    lesson_name = StringField(
        'نام درس', 
        validators=[InputRequired(message='نام درس نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'نام درس'}
    )
    grade = IntegerField(
        'پایه تحصیلی درس',  
        validators=[InputRequired(message='پایه تحصیلی درس نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'پایه تحصیلی درس'}
    )
    session= IntegerField(
        'فصل مورد نظر',  
        validators=[InputRequired(message=' فصل نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'فصل درس(به تعداد فصول درس دقت کنید)'}
    )
    q1 = TextAreaField(
        'سوال اول',
        validators=[InputRequired(message='سوال نمی تواند خالی باشد')],
        render_kw={'placeholder': 'صورت سوال اول را بنویسید'}
    )
    q2 = TextAreaField(
        'سوال دوم',
        validators=[InputRequired(message='سوال نمی تواند خالی باشد')],
        render_kw={'placeholder': 'صورت سوال دوم را بنویسید'}
    )
    q3 = TextAreaField(
        'سوال سوم',
        validators=[InputRequired(message='سوال نمی تواند خالی باشد')],
        render_kw={'placeholder': 'صورت سوال سوم را بنویسید'}
    )
    q4 = TextAreaField(
        'سوال چهارم',
        validators=[InputRequired(message='سوال نمی تواند خالی باشد')],
        render_kw={'placeholder': 'صورت سوال چهارم را بنویسید'}
    )
    q5 = TextAreaField(
        'سوال پنجم',
        validators=[InputRequired(message='سوال نمی تواند خالی باشد')],
        render_kw={'placeholder': 'صورت سوال پنجم را بنویسید'}
    )
    q6 = TextAreaField(
        'سوال ششم',
        validators=[InputRequired(message='سوال نمی تواند خالی باشد')],
        render_kw={'placeholder': 'صورت سوال ششم را بنویسید'}
    )
    q7 = TextAreaField(
        'سوال هفتم',
        validators=[InputRequired(message='سوال نمی تواند خالی باشد')],
        render_kw={'placeholder': 'صورت سوال هفتم را بنویسید'}
    )
    q8 = TextAreaField(
        'سوال هشتم',
        validators=[InputRequired(message='سوال نمی تواند خالی باشد')],
        render_kw={'placeholder': 'صورت سوال هشتم را بنویسید'}
    )
    q9 = TextAreaField(
        'سوال نهم',
        validators=[InputRequired(message='سوال نمی تواند خالی باشد')],
        render_kw={'placeholder': 'صورت سوال نهم را بنویسید'}
    )
    a1 = StringField(
        'پاسخ صحیح سوال اول',
        validators=[InputRequired(message='پاسخ سوال را مشخص کنید')],
        render_kw={'placeholder': 'پاسخ صحیح سوال اول را بنویسید'}
    )
    a2 = StringField(
        'پاسخ صحیح سوال دوم',
        validators=[InputRequired(message='پاسخ سوال را مشخص کنید')],
        render_kw={'placeholder': 'پاسخ صحیح سوال دوم را بنویسید'}
    )
    a3 = StringField(
        'پاسخ صحیح سوال سوم',
        validators=[InputRequired(message='پاسخ سوال را مشخص کنید')],
        render_kw={'placeholder': 'پاسخ صحیح سوال سوم را بنویسید'}
    )
    a4 = StringField(
        'پاسخ صحیح سوال چهارم',
        validators=[InputRequired(message='پاسخ سوال را مشخص کنید')],
        render_kw={'placeholder': 'پاسخ صحیح سوال چهارم را بنویسید'}
    )
    a5 = StringField(
        'پاسخ صحیح سوال پنجم',
        validators=[InputRequired(message='پاسخ سوال را مشخص کنید')],
        render_kw={'placeholder': 'پاسخ صحیح سوال پنجم را بنویسید'}
    )
    a6 = StringField(
        'پاسخ صحیح سوال ششم',
        validators=[InputRequired(message='پاسخ سوال را مشخص کنید')],
        render_kw={'placeholder': 'پاسخ صحیح سوال ششم را بنویسید'}
    )
    a7 = StringField(
        'پاسخ صحیح سوال هفتم',
        validators=[InputRequired(message='پاسخ سوال را مشخص کنید')],
        render_kw={'placeholder': 'پاسخ صحیح سوال هفتم را بنویسید'}
    )
    a8 = StringField(
        'پاسخ صحیح سوال هشتم',
        validators=[InputRequired(message='پاسخ سوال را مشخص کنید')],
        render_kw={'placeholder': 'پاسخ صحیح سوال هشتم را بنویسید'}
    )
    a9 = StringField(
        'پاسخ صحیح سوال نهم',
        validators=[InputRequired(message='پاسخ سوال را مشخص کنید')],
        render_kw={'placeholder': 'پاسخ صحیح سوال نهم را بنویسید'}
    )
    time = IntegerField(
        'زمان پاسخگویی',  
        validators=[InputRequired(message='زمان پاسخگویی نمی تواند خالی باشد')], 
        render_kw={'placeholder': 'زمان مجاز برای پاسخ(به دقیقه)'}
    )
    submit = SubmitField('ثبت و اضافه کردن سوالات')


class UpdateUserForm(FlaskForm):
    user_name = StringField(
        'نام کاربری', 
        render_kw={'placeholder': 'نام کاربری'}
    )
    first_name = StringField(
        'نام', 
        render_kw={'placeholder': 'نام'}
    )
    last_name = StringField(
        'نام خانوادگی', 
        render_kw={'placeholder': 'نام خانوادگی'}
    )
    grade = IntegerField(
        'پایه تحصیلی',  
        render_kw={'placeholder': 'پایه تحصیلی'}
    )
    school = StringField(
        'نام مدرسه',  
        render_kw={'placeholder': 'نام مدرسه'}
    )
    password = PasswordField(
        'رمز جدید',  
        render_kw={'placeholder': 'رمز ورود'}
    )
    re_password = PasswordField(
        'تکرار رمز جدید',  
        validators=[EqualTo('password', message='رمز ورود با تکرار رمز ورود یکسان نیست')], 
        render_kw={'placeholder': 'تکرار رمز ورود'}
    )
    submit = SubmitField('بروزرسانی')
