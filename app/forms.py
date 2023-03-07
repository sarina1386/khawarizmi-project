from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    user_name = StringField('نام کاربری', validators=[InputRequired(message="نام کاربری نمی تواند خالی باشد")], render_kw={"placeholder": "نام کاربری"})
    first_name = StringField('نام', validators=[InputRequired(message="نام خود را وارد کنید")], render_kw={"placeholder": "نام"})
    last_name = StringField('نام خانوادگی', validators=[InputRequired(message="نام خانوادگی خود را وارد کنید")], render_kw={"placeholder": "نام خانوادگی"})
    password = PasswordField('رمز عبور', validators=[InputRequired(message="یک رمز عبور انتخاب کنید"), Length(min=8, max=20, message="رمز باید حداقل 8 کاراکتر داشته اشد")], render_kw={"placeholder": "رمزعبور"})
    repeat_password = PasswordField('تکرار رمز عبور', validators=[InputRequired(message="رمز عبور خود را تکرار کنید"), EqualTo('password', message="تکرار رمز و رمز با یکدیگر یکسان نیستند!")], render_kw={"placeholder": "تکرار رمزعبور"})
    grade = IntegerField('پایه تحصیلی', validators=[InputRequired(message="پایه تحصیلی خود را وارد کنید")], render_kw={"placeholder": "پایه تحصیلی"})
    submit = SubmitField('ثبت نام')


class LoginForm(FlaskForm):
    user_name = StringField('نام کاربری', validators=[InputRequired(message="لطفا نام کاربری را وارد کنید")], render_kw={"placeholder": "نام کاربری"})
    password = PasswordField('رمزعبور', validators=[InputRequired(message="لطفا رمز عبور را وارد کنید"), Length(min=8, max=20, message="رمز عبور نمی تواند کمتر از 8 کاراکتر باشد!")], render_kw={"placeholder": "رمزعبور"})
    remember_me = BooleanField('مرا بخاطر بسپار')
    submit = SubmitField('ورود')