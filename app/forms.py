from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    user_name = StringField(
        'نام کاربری', 
        validators=[InputRequired(message='نام کاربری نمی تواند خالی باشد')], 
        render_kw={'palceholder': 'نام کاربری'}
    )
    first_name = StringField(
        'نام', 
        validators=[InputRequired(message='نام نمی تواند خالی باشد')], 
        render_kw={'palceholder': 'نام'}
    )
    last_name = StringField(
        'نام خانوادگی', 
        validators=[InputRequired(message='نام خانوادگی نمی تواند خالی باشد')], 
        render_kw={'palceholder': 'نام خانوادگی'}
    )
    grade = IntegerField(
        'پایه تحصیلی',  
        render_kw={'palceholder': 'پایه تحصیلی'}
    )
    school = StringField(
        'نام مدرسه',  
        render_kw={'palceholder': 'نام مدرسه'}
    )
    password = PasswordField(
        'رمز ورود',  
        validators=[InputRequired(message='رمز ورود نمی تواند خالی باشد')], 
        render_kw={'palceholder': 'رمز ورود'}
    )
    re_password = PasswordField(
        'تکرار رمز ورود',  
        validators=[InputRequired(message='رمز ورود نمی تواند خالی باشد'), EqualTo('password', message='رمز ورود با تکرار رمز ورود یکسان نیست')], 
        render_kw={'palceholder': 'تکرار رمز ورود'}
    )
