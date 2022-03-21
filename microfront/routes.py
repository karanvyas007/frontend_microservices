import json
from flask import render_template, url_for, redirect, flash, session, request, jsonify
from flask_login import login_required, LoginManager, login_manager
# from Microfront.models import Registration
from sqlalchemy import JSON

from Microfront.forms import RegisterForm, LoginForm, UpdateForm
import requests
from Microfront import app


@app.route('/')
def index():
    response = requests.post(f"{app.config.get('SIGNUP_URL_S')}/items")  # simple GET req
    show_data = response.json()  # response parsed in JSON
    return render_template('index.html', show_data=show_data)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global var
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        data = {
            "username": form.username.data,
            "password": form.password.data
        }
        # response = requests.post(f"{app.config.get('SIGNUP_URL_S')}/login", json=data)
        response = requests.post(f"{app.config.get('SIGNUP_URL_K')}/signin", json=data)
        var = data.get('username')
        # print(var)
        # var = response.get('username')
        if response.status_code == 200:
            response_data = json.loads(response.text)
            if response_data.get('status') == True:
                return redirect(url_for('home', var=var))
            else:
                flash("Incorrect username/password!")

    #     record = Registration.query.filter_by(username=form.username.data).first()
    #     if record and record.password == form.password.data:
    #         return redirect(url_for('home', Sno=record.Sno))
    #     else:
    #         flash("Incorrect username/password!")
    # return render_template('signin2.html', form=form)

    return render_template("signin.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        data = {
            "fullname": form.fullname.data,
            "username": form.username.data,
            "email": form.email.data,
            "password": form.confirm_password.data,
            "ph_no": form.ph_no.data
        }
        response = requests.post(f"{app.config.get('SIGNUP_URL_K')}/register", json=data)
        # response = requests.post(f"{app.config.get('SIGNUP_URL_S')}/register", json=data)
        return redirect('/signin')
    return render_template('signup.html', form=form)


@app.route('/home')
def home():
    response = requests.post("http://192.168.1.37:5004/items")  # simple GET request
    show_data = response.json()  # response parsed in JSON
    return render_template('home.html', show_data=show_data, var=var)


@app.route('/update', methods=['GET',   'POST'])
def update():
    form = UpdateForm()
    if request.method == 'POST' and form.validate_on_submit():
        data = {
            "username": form.username.data,
            "current_password": form.current_password.data,
            "new_password": form.new_password.data,
            "confirm_password": form.confirm_password.data
        }
        response = requests.post(f"{app.config.get('SIGNUP_URL_K')}/update", json=data)
        return redirect('/signin')
    return render_template('update.html',form=form)


@app.route('/delete/<var>')
def delete(var):
    response = requests.post(f"{app.config.get('SIGNUP_URL_S')}/delete", json=var)
    # record = Registration.query.filter_by(Sno=Sno).first()
    # db.session.delete(record)
    # db.session.commit()
    return redirect('/')
