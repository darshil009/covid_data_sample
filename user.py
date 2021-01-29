from flask import request, flash, url_for, render_template
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect
from app import db, user
from app import app
from app.model import user
from wtforms import validators
import json


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user_data = user.query.filter_by(email=email).first()

        if not user_data or user_data.password != password:
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))
        else:
            login_user(user_data, remember=remember)
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        state = request.form.get('state')

        user_data = user.query.filter_by(email=email).first()

        if user_data:
            flash('Email address already exists')
            return redirect(url_for('signup'))

        new_admin = user(email=email, name=name, password=password, state=state)

        db.session.add(new_admin)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    covid_data = []
    with open('state_district_wise.json') as data:
        x = json.load(data)

    state = current_user.state

    for key in x[state]['districtData']:
        if key!='Other State':
            covid_data.append([key, x[state]['districtData'][key]['active'], x[state]['districtData'][key]['confirmed'], x[state]['districtData'][key]['deceased'], x[state]['districtData'][key]['recovered']])

    return render_template('home.html', userDetails=covid_data, name=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

