import json
from flask import render_template, url_for, redirect, flash, request, session
from Microfront.forms import RegisterForm, LoginForm, UpdateForm
import requests
from Microfront import app


@app.route('/')
def index():
    """
    showing food items in card view
    :return:
        if response == 200:
        go to index page
    """
    try:
        response = requests.post(f"{app.config.get('SIGNUP_URL_K')}/food")  # simple GET req
        if response.status_code == 200:
            show_data = response.json()  # response parsed in JSON
            return render_template('index.html', show_data=show_data)
    except Exception as ex:
        print(ex)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """
        Input: Username,
               Password

    :return:
        if response == 200:
            redirect to home page
    """
    try:
        form = LoginForm()
        if request.method == 'POST' and form.validate_on_submit():
            data = {
                "username": form.username.data,
                "password": form.password.data
            }
            response = requests.post(f"{app.config.get('SIGNUP_URL_S')}/login", json=data)
            # response = requests.post(f"{app.config.get('SIGNUP_URL_K')}/signin", json=data)
            session['username'] = data.get('username')
            if response.status_code == 200:
                response_data = json.loads(response.text)
                if response_data.get('status'):
                    return redirect(url_for('home', ))
                else:
                    flash("Incorrect username/password!")
        return render_template("signin.html", form=form)

    except Exception as ex:
        print(ex)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Input: Full name,
           User name,
           Email,
           Password,
           Phone number
    :return:
        if response == 200:
            Store this details in database
            and redirect to signin page
    """
    try:
        form = RegisterForm()
        if request.method == 'POST' and form.validate_on_submit():
            data = {
                "fullname": form.fullname.data,
                "username": form.username.data,
                "email": form.email.data,
                "password": form.confirm_password.data,
                "ph_no": form.ph_no.data
            }
            # response = requests.post(f"{app.config.get('SIGNUP_URL_K')}/register", json=data)
            response = requests.post(f"{app.config.get('SIGNUP_URL_S')}/register", json=data)
            if response.status_code == 200:
                return redirect('/signin')
        return render_template('signup.html', form=form)

    except Exception as ex:
        print(ex)


@app.route('/home')
def home():
    """
        If user logged in:
            go to home page
    :return:
        all food items and loggedin username
    """
    try:
        response = requests.post(f"{app.config.get('SIGNUP_URL_S')}/items")  # simple GET request
        show_data = response.json()  # response parsed in JSON
        if 'username' in session:
            username = session['username']
            return render_template('home.html', show_data=show_data, var=username)

    except Exception as ex:
        print(ex)


@app.route('/update', methods=['GET', 'POST'])
def update():
    """
        Input: User name,
               Current Password,
               New Password
        Update password according to username at backend
    :return:
        if response == 200:
            redirect to sign in page
    """
    try:
        form = UpdateForm()
        if request.method == 'POST' and form.validate_on_submit():
            data = {
                "username": form.username.data,
                "current_password": form.current_password.data,
                "new_password": form.new_password.data,
                "confirm_password": form.confirm_password.data
            }
            response = requests.post(f"{app.config.get('SIGNUP_URL_K')}/update", json=data)
            if response.status_code == 200:
                return redirect('/signin')
        return render_template('update.html', form=form)

    except Exception as ex:
        print(ex)


@app.route('/delete')
def delete(username):
    """
        Delete user account according to username
    :param username: 'admin'
    :return:
        if response == 200:
            redirect to index page
    """
    try:
        response = requests.post(f"{app.config.get('SIGNUP_URL_S')}/delete", json=username)
        if response == 200:
            return redirect('/')

    except Exception as ex:
        print(ex)
