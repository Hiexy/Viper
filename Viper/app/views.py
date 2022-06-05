from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
from . import viper
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
        return render_template("home.html", user=current_user)


@views.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        try:
            time_s = int(request.form.get('time'))
        except:
            flash('Input is not a number!')
            return render_template("home.html", user=current_user)

        viper.scan(time_s)
        networks = viper.ap
        print(networks)
        return render_template('scanning.html', networks=networks)

    networks = viper.ap
    render_template('scanning.html', networks=networks)