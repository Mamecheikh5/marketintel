# app/dashboard_cars/views.py

from flask import render_template
from flask import request
from flask_login import login_required
from .. import db
from flask import abort, render_template
from flask_login import current_user, login_required
import pandas as pd
import numpy as np
from ..models import Car
from sqlalchemy import func
from sqlalchemy import asc, desc
from . import dashboard_cars


@dashboard_cars.route('/',)
def dashboard_carspage():
    """
    Render the homepage template on the / route
    """
    return render_template('dashboard_cars/startbootstrap-sb-admin-2-master/blank.html', title="Welcome" )


@dashboard_cars.route('/dashboard_cars', methods=['GET', 'POST'])

def dashboard():

    """
    initialisation des filtres
    """
    pays=""
    filtre_carburant=""
    filtre_transmission=""
    filtre_annee=""


    """
    Activation  des filtres s'ils sont renseignés
    """
    if request.method == 'POST':
        #suivant le filtre sur les pays
        if request.form.get('Senegal') is not None:
            pays="Sénégal"
        if request.form.get('Bénin') is not None:
            pays="Bénin"
        if request.form.get("Côte d'Ivoire") is not None:
            pays="Côte d'Ivoire"
        if request.form.get("Togo") is not None:
            pays="Togo"


        #suivant le filtre sur le type de transmission

        if request.form.get("Manuel") is not None:
            filtre_transmission="Manuel"
        if request.form.get("Non renseigné") is not None:
            filtre_transmission="Non renseigné"
        if request.form.get("Automatique") is not None:
            filtre_transmission="Automatique"


        #suivant le filtre sur le type du carburant

        if request.form.get("Gasoil") is not None:
            filtre_carburant="Gasoil"
        if request.form.get("Non renseigné") is not None:
            filtre_carburant="Non renseigné"
        if request.form.get("Essence") is not None:
            filtre_carburant="Essence"

    """
    preparation des filtre pour la bdd
    """
    payss="%"+pays+"%"
    filtre_carburant_v="%"+filtre_carburant+"%"
    filtre_transmission_v="%"+filtre_transmission+"%"
    filtre_annee_v="%"+filtre_annee+"%"








    """
    extraction des donnees relative au prix des voitures
    """




    #donnees des voitures
    ##### ensemble des donees
    cars=db.session.query(Car.constructeur,Car.modele,Car.kilometrage,Car.carburant,Car.annee,Car.localisation,Car.contact,Car.prix,Car.vendeur).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).all()
    ##### moyenne des prix des voitures
    prix=db.session.query(func.avg(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).all()





    #creation et preparation des donnees ralative aux transmissions
    #prix
    transmission=db.session.query(Car.transmission,func.avg(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.transmission).order_by(func.avg(Car.prix)).all()
    label_transmission=[]
    data_transmission=[]

    for tran in transmission:
        label_transmission.append(tran[0])
        data_transmission.append(round(tran[1]))


    #nombre
    pour_transmission=db.session.query(Car.transmission,func.count(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.transmission).order_by(func.count(Car.prix)).all()
    label_pour_transmission=[]
    data_pour_transmission=[]
    somme_transmission=0
    for pour_car in pour_transmission:
        somme_transmission+=pour_car[1]

    for pour_car in pour_transmission:
        label_pour_transmission.append(pour_car[0])
        data_pour_transmission.append(round((pour_car[1]/somme_transmission)*100))




    #creation et preparation des donnees ralative aux carburants
    #prix
    carburant=db.session.query(Car.carburant,func.avg(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.carburant).order_by(func.avg(Car.prix)).all()
    label_carburant=[]
    data_carburant=[]
    for car in carburant:
        label_carburant.append(car[0])
        data_carburant.append(round(car[1]))

    #Nombre
    pour_carburant=db.session.query(Car.carburant,func.count(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.carburant).order_by(func.count(Car.prix)).all()
    label_pour_carburant=[]
    data_pour_carburant=[]
    somme_carburant=0
    for pour_car in pour_carburant:
        somme_carburant+=pour_car[1]

    for pour_car in pour_carburant:
        label_pour_carburant.append(pour_car[0])
        data_pour_carburant.append(round((pour_car[1]/somme_carburant)*100))



    #creation et preparation des donnees ralative aux constructeurs

    #########prix
    constructeur=db.session.query(Car.constructeur,func.avg(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.constructeur).order_by(func.avg(Car.prix)).all()

    #########nombre
    pour_constructeur=db.session.query(Car.constructeur,func.count(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.constructeur).order_by(desc(func.count(Car.prix))).all()
    Top_constructeur=pour_constructeur[0]


    #creation et preparation des donnees ralative aux constructeurs-model
    #########prix
    constructeur_modele=db.session.query(Car.constructeur,Car.modele,func.avg(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.constructeur,Car.modele).order_by(func.avg(Car.prix)).all()
    #########nombre
    pour_constructeur_modele=db.session.query(Car.constructeur,Car.modele,func.count(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.constructeur,Car.modele).order_by(desc(func.count(Car.prix))).all()
    Top_constructeur_model=pour_constructeur_modele[0]

    #creation et preparation des donnees ralative aux vendeurs
    #########prix
    vendeur=db.session.query(Car.vendeur,func.avg(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.vendeur).order_by(desc(func.avg(Car.prix))).all()
    #########nombre
    pour_vendeur=db.session.query(Car.vendeur,func.count(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.vendeur).order_by(desc(func.count(Car.prix))).all()
    Top_vendeur=pour_vendeur[0]




    #creation et preparation des donnees ralative aux annees
    #########prix
    annee=db.session.query(Car.annee,func.avg(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.annee).order_by(Car.annee).all()
    label_annee=[]
    data_annee=[]
    for an in annee:
        label_annee.append(an[0])
        data_annee.append(an[1])
    #########nombre
    pour_annee=db.session.query(Car.annee,func.count(Car.prix)).filter(Car.localisation.like(payss),Car.carburant.like(filtre_carburant_v),Car.transmission.like(filtre_transmission_v)).group_by(Car.annee).order_by(Car.annee).all()

    label_pour_annee=[]
    data_pour_annee=[]
    for an in annee:
        label_pour_annee.append(an[0])
        data_pour_annee.append(an[1])


    return render_template('dashboard_cars/startbootstrap-sb-admin-2-master/index.html',pays=pays, title="Dashboard",annee=annee,transmission=transmission,carburant=carburant,constructeur_modele=constructeur_modele,constructeur=constructeur,label_annee=label_annee,data_annee=data_annee,label_transmission=label_transmission,data_transmission=data_transmission,prix=round(prix[0][0]),label_carburant=label_carburant,data_carburant=data_carburant,label_pour_carburant=label_pour_carburant,data_pour_carburant=data_pour_carburant,label_pour_transmission=label_pour_transmission,data_pour_transmission=data_pour_transmission,Top_constructeur_model=Top_constructeur_model,Top_constructeur=Top_constructeur,filtre_transmission=filtre_transmission,filtre_carburant=filtre_carburant,Top_vendeur=Top_vendeur,cars=cars)






# creation de la page admin
@dashboard_cars.route('/admin/dashboard', methods=['GET', 'POST'])

def admin_dashboard():
    # page a afficher si on a pas les droits
    if not current_user.is_admin:
        abort(403)

    return render_template('cars/dashboard_cars/startbootstrap-sb-admin-2-master/index.html', title="Dashboard")
