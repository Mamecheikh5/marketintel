# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from . import acceuil
from .. import db
from ..models import Employee


@acceuil.route('/', methods=['GET', 'POST'])
def accueil():
    
    return render_template('acceuil.html', title='Register')


