# app/home/views.py

from flask import render_template
from flask_login import login_required
from flask import abort, render_template
from flask_login import current_user, login_required
from sqlalchemy import func



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
        r = form.recherche.data
        search = "%{}%".format(r)
        
        restaurant = restaurants.query.filter(restaurants.nom.like(search)).all()
        if form.filtre.data == '1':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='senegal').all()
        if form.filtre.data == '2':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='benin').all()
        if form.filtre.data == '3':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='cote-divoire').all()
        if form.filtre.data == '4':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='burkina').all()
        if form.filtre.data == '5':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='togo').all()
        
        
    """
    Render the dashboard template on the /recherche route
    """
    return render_template('home/recherche.html',form=form, restaurant=restaurant, title="Recherche")

@home.route('/recherche/<string:nom>', methods=['GET', 'POST'])
@login_required
def regarder(nom):
    # prevent non-admins from accessing the page

    r = restaurants.query.filter_by(nom=nom).first()
    form=rechercherForm()
    restaurant=None
    
    if form.validate_on_submit():
        r = form.recherche.data
        search = "%{}%".format(r)
        restaurant = restaurants.query.filter(restaurants.nom.like(search)).all()
        if form.filtre.data == '1':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='senegal').all()
        if form.filtre.data == '2':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='benin').all()
        if form.filtre.data == '3':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='cote-divoire').all()
        if form.filtre.data == '4':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='burkina').all()
        if form.filtre.data == '5':
            restaurant = restaurants.query.filter(restaurants.nom.like(search)).filter_by(pays='togo').all()
        

    return render_template('home/recherche.html', title="restaurant" ,form=form, r=r,restaurant=restaurant )

@home.route('/statistiques', methods=['GET', 'POST'])
@login_required
def donnee():
    # prevent non-admins from accessing the page
    

    Dakar = restaurants.query.filter_by(region='Dakar').count()
    Saint = restaurants.query.filter_by(region='Saint-Louis').count()
    Mbour= restaurants.query.filter_by(region="M'bour").count()
    senegal=[Dakar,Saint,Mbour]
    Abomey = restaurants.query.filter_by(region='Abomey-Calavi').count()
    Bohicon = restaurants.query.filter_by(region='Bohicon').count()
    Porto = restaurants.query.filter_by(region='Porto-Novo').count()
    Cotonou = restaurants.query.filter_by(region='Cotonou').count()
   
    benin=[Cotonou,Abomey,Bohicon,Porto]
    Grand=restaurants.query.filter_by(region='Grand-Bassam').count()
    Yamoussoukro=restaurants.query.filter_by(region='Yamoussoukro').count()
    Abidjan = restaurants.query.filter_by(region='Abidjan').count()
   
    cote=[Abidjan,Yamoussoukro,Grand]
    
    Koudougou=restaurants.query.filter_by(region='Koudougou').count()
    Bobo=restaurants.query.filter_by(region='Bobo-Dioulasso').count()
    ouagadougou=restaurants.query.filter_by(region='Ouagadougou').count()
    burkina=[ouagadougou,Bobo,Koudougou]

    
    lome=restaurants.query.filter_by(region='Lomé').count()
    Atakpame=restaurants.query.filter_by(region='Atakpamé').count()
    Kpalime=restaurants.query.filter_by(region='Kpalimé').count()
    togo=[lome,Atakpame,Kpalime]
    
    return render_template('home/statistique.html', title="Statistiques" ,cote=cote, senegal=senegal,benin=benin,burkina=burkina,togo=togo)


@home.route('/capitale', methods=['GET', 'POST'])
@login_required
def Max():
    Dakar = restaurants.query.filter_by(region='Dakar').count()
    Ouagadougou = restaurants.query.filter_by(region='Ouagadougou').count()
    Lome= restaurants.query.filter_by(region="Lomé").count()
    Abidjan = restaurants.query.filter_by(region='Abidjan').count()
    Cotonou = restaurants.query.filter_by(region='Cotonou').count()
    nombres=[Dakar,Lome,Ouagadougou,Abidjan,Cotonou]
    return render_template('home/capitale.html', title="Statistiques" ,nombres=nombres )
    
    
