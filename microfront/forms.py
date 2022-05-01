from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField, EmailField
from wtforms.validators import InputRequired, EqualTo, DataRequired


class RegisterForm(FlaskForm):
    fullname = StringField("Full Name", validators=[DataRequired()], render_kw={"placeholder": "fullname"})
    username = StringField("User Name", validators=[DataRequired()], render_kw={"placeholder": "username"})
    email = EmailField("Email Id", validators=[DataRequired()], render_kw={"placeholder": "email"})
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm_password')],
                             render_kw={"placeholder": "password"})
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()],
                                     render_kw={"placeholder": "confirm password"})
    ph_no = TelField("Mobile Number", validators=[DataRequired()], render_kw={"placeholder": "Mobile Number"})
    submit = SubmitField("Registered Successfully!")


class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired()], render_kw={"placeholder": "username"})
    password = PasswordField("Password", validators=[InputRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login Successfully!")


class UpdateForm(FlaskForm):
    username = StringField("username", render_kw={"placeholder": "username"})
    current_password = PasswordField("current Password", render_kw={"placeholder": "current password"})
    new_password = PasswordField("New Password", validators=[EqualTo("confirm_password")],
                                 render_kw={"placeholder": "new password"})
    confirm_password = PasswordField("Confirm Password",
                                     render_kw={"placeholder": "confirm password"})
    submit = SubmitField("Login Successfully!")

