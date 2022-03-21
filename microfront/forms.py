from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField, EmailField
from wtforms.validators import InputRequired, ValidationError, EqualTo, DataRequired


# from CampFood.models import Registration


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

    '''
    def validate_fullname(self, fullname):
        name = str(fullname.data).split()

        # Check if user already exist -> fullname_correct is not None. If found then fullname_correct can't be None
        if len(name) != 2:
            raise ValidationError("Must Enter Firstname and Lastname only. Try another!!")
        elif not (name[0].isalpha() and name[1].isalpha()):
            raise ValidationError("Invalid! Only alphabets are allowed!")
    '''

    # def validate_username(self, username):
    #     username_exist = Registration.query.filter_by(username=username.data).first()
    #     if username_exist:
    #         raise ValidationError("This username Already exist. Try another!!")
    #
    # def validate_ph_no(self, ph_no):
    #     ph_no_exist = Registration.query.filter_by(ph_no=ph_no.data).first()
    #     if ph_no_exist:
    #         raise ValidationError("This phone number Already exist. Try another!!")

    '''
    def validate_password(self, password):
        if len(str(password.data)) < 8:
            raise ValidationError("Make your password atleast 8 characters! ")

    '''


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

