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