from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from sqlalchemy import func
from . import defimobilier
from .. import db
from sqlalchemy import desc, asc

from ..models import Immobilier

@defimobilier.route('/immodashboard', methods=['GET'])
def immodashboard():
    offres = Immobilier.query.all()
    return render_template('immodashboard/dashboard.html',offres=offres)


@defimobilier.route('/immodashboard/togo', methods=['GET'])
def togo():
    """
        Dashboard of Togo
    """
    choix = db.session.query(Immobilier.city, func.count(Immobilier.city)).filter(Immobilier.country.contains('Togo')).group_by(Immobilier.city).all()
    max_price = []
    min_price = []

    datas = []
    labels = []

    for offre in choix:
        datas.append(offre[1])
        labels.append(offre[0])
        city = db.session.query(func.min(Immobilier.price),func.max(Immobilier.price)).filter(Immobilier.city==offre[0]).all()
        max_price.append(city[0][1])
        min_price.append(city[0][0])

    return render_template('immodashboard/togo.html',choix=choix, labels=labels, datas=datas, min_price=min_price, max_price=max_price)

@defimobilier.route('/immodashboard/cameroun', methods=['GET'])
def cameroun():
    """
        Dashboard of Caméroun
    """
    choix = db.session.query(Immobilier.city, func.count(Immobilier.city)).filter(Immobilier.country.contains('Caméroun')).group_by(Immobilier.city).all()
    max_price = []
    min_price = []

    datas = []
    labels = []

    for offre in choix:
        datas.append(offre[1])
        labels.append(offre[0])
        city = db.session.query(func.min(Immobilier.price),func.max(Immobilier.price)).filter(Immobilier.city==offre[0]).all()
        max_price.append(city[0][1])
        min_price.append(city[0][0])

    return render_template('immodashboard/cameroun.html',choix=choix, labels=labels, datas=datas, min_price=min_price, max_price=max_price)

@defimobilier.route('/immodashboard/benin', methods=['GET'])
def benin():
    """
        Dashboard of Bénin
    """
    choix = db.session.query(Immobilier.city, func.count(Immobilier.city)).filter(Immobilier.country.contains('Bénin')).group_by(Immobilier.city).all()
    max_price = []
    min_price = []

    datas = []
    labels = []

    for offre in choix:
        datas.append(offre[1])
        labels.append(offre[0])
        city = db.session.query(func.min(Immobilier.price),func.max(Immobilier.price)).filter(Immobilier.city==offre[0]).all()
        max_price.append(city[0][1])
        min_price.append(city[0][0])

    return render_template('immodashboard/benin.html',choix=choix, labels=labels, datas=datas, min_price=min_price, max_price=max_price)

@defimobilier.route('/immodashboard/burkina', methods=['GET'])
def burkina():
    """
        Dashboard of Burkina
    """
    choix = db.session.query(Immobilier.city, func.count(Immobilier.city)).filter(Immobilier.country.contains('Burkina')).group_by(Immobilier.city).all()
    max_price = []
    min_price = []

    datas = []
    labels = []

    for offre in choix:
        datas.append(offre[1])
        labels.append(offre[0])
        city = db.session.query(func.min(Immobilier.price),func.max(Immobilier.price)).filter(Immobilier.city==offre[0]).all()
        max_price.append(city[0][1])
        min_price.append(city[0][0])

    return render_template('immodashboard/togo.html',choix=choix, labels=labels, datas=datas, min_price=min_price, max_price=max_price)

@defimobilier.route('/immodashboard/cotedivoire', methods=['GET'])
def cotedivoire():
    """
        Dashboard of Côte d'Ivoire
    """
    choix = db.session.query(Immobilier.city, func.count(Immobilier.city)).filter(Immobilier.country.contains("Côte d'Ivoire")).group_by(Immobilier.city).all()
    max_price = []
    min_price = []

    datas = []
    labels = []

    for offre in choix:
        datas.append(offre[1])
        labels.append(offre[0])
        city = db.session.query(func.min(Immobilier.price),func.max(Immobilier.price)).filter(Immobilier.city==offre[0]).all()
        max_price.append(city[0][1])
        min_price.append(city[0][0])

    return render_template('immodashboard/cotedivoire.html',choix=choix, labels=labels, datas=datas, min_price=min_price, max_price=max_price)

@defimobilier.route('/immodashboard/maroc', methods=['GET'])
def maroc():
    """
        Dashboard of Maroc
    """
    choix = db.session.query(Immobilier.city, func.count(Immobilier.city), func.sum(Immobilier.price)).filter(Immobilier.country.contains("Maroc")).group_by(Immobilier.city).all()
    max_price = []
    min_price = []
    sums = []
    average = {}
    avg_labels = []
    avg_price = [] 
    datas = []
    labels = []

    for offre in choix:
        if offre[2] is not None:
            datas.append(offre[1])
            labels.append(offre[0])
            city = db.session.query(func.min(Immobilier.price),func.max(Immobilier.price)).filter(Immobilier.city==offre[0]).all()
            max_price.append(city[0][1])
            min_price.append(city[0][0])
            sums.append(offre[2])
            average[offre[0]] = offre[2]//offre[1]

    sort_average = sorted(average.items(), key=lambda x: x[1])
    for avg in sort_average:
        avg_labels.append(avg[0])
        avg_price.append(avg[1])
        print(avg[1],"for avg 1 ", avg[0]  )
    
    avg_price_data=[]
    for i in avg_price:
        avg_price_data.append(float(i))
    avg_price=avg_price_data


    max = db.session.query(Immobilier.city,func.max(Immobilier.price)).filter(Immobilier.country.contains("Maroc")).group_by(Immobilier.city).order_by(desc(func.max(Immobilier.price))).first()
    min = db.session.query(Immobilier.city,func.min(Immobilier.price)).filter(Immobilier.country.contains("Maroc")).group_by(Immobilier.city).order_by(asc(func.max(Immobilier.price))).first()
    

    return render_template('immodashboard/maroc.html',offres=choix, datas=datas, labels=labels, max_price=max_price, min_price=min_price, sums=sums, average=avg_price, avg_labels=avg_labels, max=max, min=min)

@defimobilier.route('/immodashboard/tunisie', methods=['GET'])
def tunisie():
    """
        Dashboard of Maroc
    """
    choix = db.session.query(Immobilier.city, func.count(Immobilier.city), func.sum(Immobilier.price)).filter(Immobilier.country.contains("Tunisie")).group_by(Immobilier.city).all()
    max_price = []
    min_price = []
    sums = []
    average = {}
    avg_labels = []
    avg_price = [] 
    datas = []
    labels = []

    for offre in choix:
        if offre[2] is not None:
            datas.append(offre[1])
            labels.append(offre[0])
            city = db.session.query(func.min(Immobilier.price),func.max(Immobilier.price)).filter(Immobilier.city==offre[0]).all()
            max_price.append(city[0][1])
            min_price.append(city[0][0])
            sums.append(offre[2])
            average[offre[0]] = offre[2]//offre[1]

    sort_average = sorted(average.items(), key=lambda x: x[1])
    for avg in sort_average:
        avg_labels.append(avg[0])
        avg_price.append(avg[1])
        print(avg[1],"for avg 1 ", avg[0]  )
    
    avg_price_data=[]
    for i in avg_price:
        avg_price_data.append(float(i))
    avg_price=avg_price_data


    max = db.session.query(Immobilier.city,func.max(Immobilier.price)).filter(Immobilier.country.contains("Tunisie")).group_by(Immobilier.city).order_by(desc(func.max(Immobilier.price))).first()
    min = db.session.query(Immobilier.city,func.min(Immobilier.price)).filter(Immobilier.country.contains("Tunisie")).group_by(Immobilier.city).order_by(asc(func.max(Immobilier.price))).first()
    

    return render_template('immodashboard/tunisie.html',offres=choix, datas=datas, labels=labels, max_price=max_price, min_price=min_price, sums=sums, average=avg_price, avg_labels=avg_labels, max=max, min=min)

@defimobilier.route('/immodashboard/algerie', methods=['GET'])
def algerie():
    """
        Dashboard of Maroc
    """
    choix = db.session.query(Immobilier.city, func.count(Immobilier.city), func.sum(Immobilier.price)).filter(Immobilier.country.contains("Algérie")).group_by(Immobilier.city).all()
    max_price = []
    min_price = []
    sums = []
    average = {}
    avg_labels = []
    avg_price = [] 
    datas = []
    labels = []

    for offre in choix:
        if offre[2] is not None:
            datas.append(offre[1])
            labels.append(offre[0])
            city = db.session.query(func.min(Immobilier.price),func.max(Immobilier.price)).filter(Immobilier.city==offre[0]).all()
            max_price.append(city[0][1])
            min_price.append(city[0][0])
            sums.append(offre[2])
            average[offre[0]] = offre[2]//offre[1]

    sort_average = sorted(average.items(), key=lambda x: x[1])
    for avg in sort_average:
        avg_labels.append(avg[0])
        avg_price.append(avg[1])
        print(avg[1],"for avg 1 ", avg[0]  )
    
    avg_price_data=[]
    for i in avg_price:
        avg_price_data.append(float(i))
    avg_price=avg_price_data


    max = db.session.query(Immobilier.city,func.max(Immobilier.price)).filter(Immobilier.country.contains("Algérie")).group_by(Immobilier.city).order_by(desc(func.max(Immobilier.price))).first()
    min = db.session.query(Immobilier.city,func.min(Immobilier.price)).filter(Immobilier.country.contains("Algérie")).group_by(Immobilier.city).order_by(asc(func.max(Immobilier.price))).first()
    

    return render_template('immodashboard/algerie.html',offres=choix, datas=datas, labels=labels, max_price=max_price, min_price=min_price, sums=sums, average=avg_price, avg_labels=avg_labels, max=max, min=min)