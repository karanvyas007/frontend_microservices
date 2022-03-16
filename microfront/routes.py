import json

from flask import render_template, url_for, redirect, flash, session, request, jsonify
from flask_login import login_required, LoginManager, login_manager
# from Microfront.models import Registration, Items
from sqlalchemy import JSON

from Microfront.forms import RegisterForm
import requests

# from Microfront import db
from Microfront import app


@app.route('/')
def Micro():
    response = requests.post("http://192.168.1.37:5004/test_t")  # simple GET req
    # print(response)
    show_data = response.json()  # response parsed in JSON
    # print(show_data)
    return render_template('index.html', show_data=show_data)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        data = {
            "fullname": form.fullname.data,
            "username": form.username.data,
            "password": form.confirm_password.data,
            "ph_no": form.ph_no.data
        }

        response = requests.post(f"{app.config.get('BACKEND_URL')}/register", data=data)
        # response = requests.get(f"{app.config.get('BACKEND_URL')}/register")
        return json.dumps(response)
        # response_json = response.jso n()
        # return jsonify(response_json=response_json)
    return render_template('signup.html', form=form)
