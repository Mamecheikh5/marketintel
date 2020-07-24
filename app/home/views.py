# app/home/views.py

from flask import render_template
from flask_login import login_required
from flask import abort, render_template
from flask_login import current_user, login_required



from . import home
from .forms import rechercherForm

from ..models import restaurants

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/recherche', methods=['GET', 'POST'])
@login_required
def recherche():
    form=rechercherForm()
    restaurant=None
    if form.validate_on_submit():
        restaurant = restaurants.query.filter_by(nom=form.recherche.data).first()
        
    """
    Render the dashboard template on the /recherche route
    """
    return render_template('home/recherche.html',form=form, restaurant=restaurant, title="Recherche")

@home.route('/restaurant/<string:nom>', methods=['GET', 'POST'])
@login_required
def regarder(nom):
    # prevent non-admins from accessing the page
    
    restaurant = restaurants.query.filter_by(nom=nom).first()

    return render_template('home/restaurant.html', title="restaurant" , restaurant=restaurant )



