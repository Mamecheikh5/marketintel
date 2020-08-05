from flask import render_template, request
from flask_login import login_required,current_user
from sqlalchemy.orm import sessionmaker

from . import home
from ..models import Offre

@home.route('/emploi/md')
def md():
    offres_list = Offre.query.limit(10).all()

    Toffres = Offre.query.all()
    nbreOffres = 0
    for offre in Toffres:
        nbreOffres = nbreOffres + 1

    nbrePays = 9

    secteurs = ["informatique","Santé","Commerce","Gestion","Agriculture","Restauration","Transport","Justice","Administration","Environnement","Vente","Ressources Humaines","Industrie","Marketing","Services","Batiment"]
    ns = 0
    for sect in secteurs:
        i = Offre.query.filter(Offre.secteur.like("%sect%")).count
        if i!=0:
            ns = ns + 1

    #type de contrat
    nbreCDI = Offre.query.filter(Offre.typeContrat.like("%CDI%")).count()
    pourcentageCDI = round(nbreCDI/nbreOffres*100)

    nbreCDD = Offre.query.filter(Offre.typeContrat.like("%CDD%")).count()
    pourcentageCDD = round(nbreCDD/nbreOffres*100)

    nbreStage = Offre.query.filter(Offre.typeContrat.like("%Stage%")).count()
    pourcentageStage = round(nbreStage/nbreOffres*100)

    nbreAlternance = Offre.query.filter(Offre.typeContrat.like("%Alternance%")).count()
    pourcentageAlternance = round(nbreAlternance/nbreOffres*100)

    nbreFreelance = Offre.query.filter(Offre.typeContrat.like("%Freelance%")).count()
    pourcentageFreelance = round(nbreFreelance/nbreOffres*100)

    #secteur
    nbreInf = Offre.query.filter(Offre.secteur.like("%Informatique%")).count()
    pourcentageInf = round(nbreInf/nbreOffres*100)

    nbreVente = Offre.query.filter(Offre.secteur.like("%Vente%")).count()
    pourcentageVente = round(nbreVente/nbreOffres*100)

    nbreBatiment = Offre.query.filter(Offre.secteur.like("%Batiment%")).count()
    pourcentageBatiment = round(nbreBatiment/nbreOffres*100)

    nbreInd = Offre.query.filter(Offre.secteur.like("%Electrique%")).count()
    pourcentageInd = round(nbreInd/nbreOffres*100)

    nbreSante = Offre.query.filter(Offre.secteur.like("%Sante%")).count()
    pourcentageSante = round(nbreSante/nbreOffres*100)

    nbrEnv = Offre.query.filter(Offre.secteur.like("%Agriculture%")).count()
    pourcentageEnv = round(nbrEnv/nbreOffres*100)

    return render_template("dashboard/index.html",offres=offres_list,no=nbreOffres,np=nbrePays,ns=ns,cdi=pourcentageCDI,cdd=pourcentageCDD,stage=pourcentageStage,alternance=pourcentageAlternance,freelance=pourcentageFreelance,inf=pourcentageInf,vente=pourcentageVente,batiment=pourcentageBatiment,industrie=pourcentageInd,sante=pourcentageSante,env=pourcentageEnv)


@home.route('/emploi/md/<pays>/')
def p(pays):
    offres_list = Offre.query.filter_by(pays=pays).limit(10)

    Toffres = Offre.query.filter_by(pays=pays)
    nbreOffres = 0
    for offre in Toffres:
        nbreOffres = nbreOffres + 1
    nbOffres = nbreOffres
    if nbreOffres == 0:
        nbreOffres = 1

    nbrePays = 1

    secteurs = ["informatique","Santé","Commerce","Gestion","Agriculture","Restauration","Transport","Justice","Administration","Environnement","Vente","Ressources Humaines","Industrie","Marketing","Services","Batiment"]
    ns = 0
    for sect in secteurs:
        i = Offre.query.filter(Offre.secteur.like("%sect%")).filter_by(pays=pays).count
        if i!=0:
            ns = ns + 1

    #type de contrat
    nbreCDI = Offre.query.filter(Offre.typeContrat.like("%CDI%")).filter_by(pays=pays).count()
    pourcentageCDI = round(nbreCDI/nbreOffres*100)

    nbreCDD = Offre.query.filter(Offre.typeContrat.like("%CDD%")).filter_by(pays=pays).count()
    pourcentageCDD = round(nbreCDD/nbreOffres*100)

    nbreStage = Offre.query.filter(Offre.typeContrat.like("%Stage%")).filter_by(pays=pays).count()
    pourcentageStage = round(nbreStage/nbreOffres*100)

    nbreAlternance = Offre.query.filter(Offre.typeContrat.like("%Alternance%")).filter_by(pays=pays).count()
    pourcentageAlternance = round(nbreAlternance/nbreOffres*100)

    nbreFreelance = Offre.query.filter(Offre.typeContrat.like("%Freelance%")).filter_by(pays=pays).count()
    pourcentageFreelance = round(nbreFreelance/nbreOffres*100)

    #secteur
    nbreInf = Offre.query.filter(Offre.secteur.like("%Informatique%")).filter_by(pays=pays).count()
    pourcentageInf = round(nbreInf/nbreOffres*100)

    nbreVente = Offre.query.filter(Offre.secteur.like("%Vente%")).filter_by(pays=pays).count()
    pourcentageVente = round(nbreVente/nbreOffres*100)

    nbreBatiment = Offre.query.filter(Offre.secteur.like("%Batiment%")).filter_by(pays=pays).count()
    pourcentageBatiment = round(nbreBatiment/nbreOffres*100)

    nbreInd = Offre.query.filter(Offre.secteur.like("%Electrique%")).filter_by(pays=pays).count()
    pourcentageInd = round(nbreInd/nbreOffres*100)

    nbreSante = Offre.query.filter(Offre.secteur.like("%Sante%")).filter_by(pays=pays).count()
    pourcentageSante = round(nbreSante/nbreOffres*100)

    nbrEnv = Offre.query.filter(Offre.secteur.like("%Agriculture%")).filter_by(pays=pays).count()
    pourcentageEnv = round(nbrEnv/nbreOffres*100)


    return render_template("dashboard/pays.html",offres=offres_list,no=nbOffres,np=nbrePays,ns=ns,cdi=pourcentageCDI,cdd=pourcentageCDD,stage=pourcentageStage,alternance=pourcentageAlternance,freelance=pourcentageFreelance,inf=pourcentageInf,vente=pourcentageVente,batiment=pourcentageBatiment,industrie=pourcentageInd,sante=pourcentageSante,env=pourcentageEnv,pays=pays)


@home.route('/emploi/md/secteur/<sect>')
def s(sect):
    offres_list = Offre.query.filter(Offre.secteur.like("%"+sect+"%")).limit(10)

    Toffres = Offre.query.filter(Offre.secteur.like("%"+sect+"%"))
    nbreOffres = 0
    for offre in Toffres:
        nbreOffres = nbreOffres + 1
    nbOffres = nbreOffres
    if nbreOffres == 0:
        nbreOffres = 1

    ns=1

    pays = ["Algerie","Senegal","France","Benin","Cameroun","Maroc","Cote d'Ivoire","Congo","Tunisie"]
    nbrePays = 0
    for p in pays:
        i = Offre.query.filter(Offre.pays.like("%"+p+"%")).filter(Offre.secteur.like("%"+sect+"%")).count()
        if i!=0:
            nbrePays = nbrePays + 1

    #type de contrat
    nbreCDI = Offre.query.filter(Offre.typeContrat.like("%CDI%")).filter(Offre.secteur.like("%"+sect+"%")).count()
    pourcentageCDI = round(nbreCDI/nbreOffres*100)

    nbreCDD = Offre.query.filter(Offre.typeContrat.like("%CDD%")).filter(Offre.secteur.like("%"+sect+"%")).count()
    pourcentageCDD = round(nbreCDD/nbreOffres*100)

    nbreStage = Offre.query.filter(Offre.typeContrat.like("%Stage%")).filter(Offre.secteur.like("%"+sect+"%")).count()
    pourcentageStage = round(nbreStage/nbreOffres*100)

    nbreAlternance = Offre.query.filter(Offre.typeContrat.like("%Alternance%")).filter(Offre.secteur.like("%"+sect+"%")).count()
    pourcentageAlternance = round(nbreAlternance/nbreOffres*100)

    nbreFreelance = Offre.query.filter(Offre.typeContrat.like("%Freelance%")).filter(Offre.secteur.like("%"+sect+"%")).count()
    pourcentageFreelance = round(nbreFreelance/nbreOffres*100)

    #secteur
    nbreInf = Offre.query.filter(Offre.secteur.like("%Informatique%")).count()
    pourcentageInf = round(nbreInf/nbreOffres*100)

    nbreVente = Offre.query.filter(Offre.secteur.like("%Vente%")).count()
    pourcentageVente = round(nbreVente/nbreOffres*100)

    nbreBatiment = Offre.query.filter(Offre.secteur.like("%Batiment%")).count()
    pourcentageBatiment = round(nbreBatiment/nbreOffres*100)

    nbreInd = Offre.query.filter(Offre.secteur.like("%Electrique%")).count()
    pourcentageInd = round(nbreInd/nbreOffres*100)

    nbreSante = Offre.query.filter(Offre.secteur.like("%Sante%")).count()
    pourcentageSante = round(nbreSante/nbreOffres*100)

    nbrEnv = Offre.query.filter(Offre.secteur.like("%Agriculture%")).count()
    pourcentageEnv = round(nbrEnv/nbreOffres*100)

    return render_template("dashboard/secteur.html",offres=offres_list,no=nbOffres,np=nbrePays,ns=ns,cdi=pourcentageCDI,cdd=pourcentageCDD,stage=pourcentageStage,alternance=pourcentageAlternance,freelance=pourcentageFreelance,inf=pourcentageInf,vente=pourcentageVente,batiment=pourcentageBatiment,industrie=pourcentageInd,sante=pourcentageSante,env=pourcentageEnv,secteur=sect)


@home.route('/emploi/md/pays_secteur/<pays>/<secteur>')
def pays_secteur(pays,secteur):
    offres_list = Offre.query.filter(Offre.secteur.like("%"+secteur+"%")).filter_by(pays=pays).limit(10)

    Toffres = Offre.query.filter(Offre.secteur.like("%"+secteur+"%")).filter_by(pays=pays)
    nbreOffres = 0
    for offre in Toffres:
        nbreOffres = nbreOffres + 1
    nbOffres = nbreOffres
    if nbreOffres == 0:
        nbreOffres = 1

    ns = 1

    nbrePays = 1

    #type de contrat
    nbreCDI = Offre.query.filter(Offre.typeContrat.like("%CDI%")).filter(Offre.secteur.like("%"+secteur+"%")).filter_by(pays=pays).count()
    pourcentageCDI = round(nbreCDI/nbreOffres*100)

    nbreCDD = Offre.query.filter(Offre.typeContrat.like("%CDD%")).filter(Offre.secteur.like("%"+secteur+"%")).filter_by(pays=pays).count()
    pourcentageCDD = round(nbreCDD/nbreOffres*100)

    nbreStage = Offre.query.filter(Offre.typeContrat.like("%Stage%")).filter(Offre.secteur.like("%"+secteur+"%")).filter_by(pays=pays).count()
    pourcentageStage = round(nbreStage/nbreOffres*100)

    nbreAlternance = Offre.query.filter(Offre.typeContrat.like("%Alternance%")).filter(Offre.secteur.like("%"+secteur+"%")).filter_by(pays=pays).count()
    pourcentageAlternance = round(nbreAlternance/nbreOffres*100)

    nbreFreelance = Offre.query.filter(Offre.typeContrat.like("%Freelance%")).filter(Offre.secteur.like("%"+secteur+"%")).filter_by(pays=pays).count()
    pourcentageFreelance = round(nbreFreelance/nbreOffres*100)

    #secteur
    nbreInf = Offre.query.filter(Offre.secteur.like("%Informatique%")).filter_by(pays=pays).count()
    pourcentageInf = round(nbreInf/nbreOffres*100)

    nbreVente = Offre.query.filter(Offre.secteur.like("%Vente%")).filter_by(pays=pays).count()
    pourcentageVente = round(nbreVente/nbreOffres*100)

    nbreBatiment = Offre.query.filter(Offre.secteur.like("%Batiment%")).filter_by(pays=pays).count()
    pourcentageBatiment = round(nbreBatiment/nbreOffres*100)

    nbreInd = Offre.query.filter(Offre.secteur.like("%Electrique%")).filter_by(pays=pays).count()
    pourcentageInd = round(nbreInd/nbreOffres*100)

    nbreSante = Offre.query.filter(Offre.secteur.like("%Sante%")).filter_by(pays=pays).count()
    pourcentageSante = round(nbreSante/nbreOffres*100)

    nbrEnv = Offre.query.filter(Offre.secteur.like("%Agriculture%")).filter_by(pays=pays).count()
    pourcentageEnv = round(nbrEnv/nbreOffres*100)

    return render_template("dashboard/pays_secteur.html",offres=offres_list,no=nbOffres,np=nbrePays,ns=ns,cdi=pourcentageCDI,cdd=pourcentageCDD,stage=pourcentageStage,alternance=pourcentageAlternance,freelance=pourcentageFreelance,inf=pourcentageInf,vente=pourcentageVente,batiment=pourcentageBatiment,industrie=pourcentageInd,sante=pourcentageSante,env=pourcentageEnv,pays=pays,secteur=secteur)

@home.route('/emploi/md/rechercheInt',methods=["POST"])
def rechercheInt():
    offres_list = Offre.query.filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).limit(15)

    Toffres = Offre.query.filter(Offre.intitule.like("%"+request.form.get('intitule')+"%"))
    nbreOffres = 0
    for offre in Toffres:
        nbreOffres = nbreOffres + 1
    nbOffres = nbreOffres
    if nbreOffres == 0:
        nbreOffres = 1

    secteurs = ["informatique","Santé","Commerce","Gestion","Agriculture","Restauration","Transport","Justice","Administration","Environnement","Vente","Ressources Humaines","Industrie","Marketing","Services","Batiment"]
    ns = 0
    for sect in secteurs:
        i = Offre.query.filter(Offre.secteur.like("%sect%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%"))
        if i!=0:
            ns = ns + 1

    pays = ["Algerie","Senegal","France","Benin","Cameroun","Maroc","Cote d'Ivoire","Congo","Tunisie"]
    nbrePays = 0
    for p in pays:
        i = Offre.query.filter(Offre.pays.like("%p%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count
        if i!=0:
            nbrePays = nbrePays + 1


    #type de contrat
    nbreCDI = Offre.query.filter(Offre.typeContrat.like("%CDI%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageCDI = round(nbreCDI/nbreOffres*100)

    nbreCDD = Offre.query.filter(Offre.typeContrat.like("%CDD%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageCDD = round(nbreCDD/nbreOffres*100)

    nbreStage = Offre.query.filter(Offre.typeContrat.like("%Stage%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageStage = round(nbreStage/nbreOffres*100)

    nbreAlternance = Offre.query.filter(Offre.typeContrat.like("%Alternance%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageAlternance = round(nbreAlternance/nbreOffres*100)

    nbreFreelance = Offre.query.filter(Offre.typeContrat.like("%Freelance%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageFreelance = round(nbreFreelance/nbreOffres*100)

    #secteur
    nbreInf = Offre.query.filter(Offre.secteur.like("%Informatique%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageInf = round(nbreInf/nbreOffres*100)

    nbreVente = Offre.query.filter(Offre.secteur.like("%Vente%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageVente = round(nbreVente/nbreOffres*100)

    nbreBatiment = Offre.query.filter(Offre.secteur.like("%Batiment%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageBatiment = round(nbreBatiment/nbreOffres*100)

    nbreInd = Offre.query.filter(Offre.secteur.like("%Electrique%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageInd = round(nbreInd/nbreOffres*100)

    nbreSante = Offre.query.filter(Offre.secteur.like("%Sante%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageSante = round(nbreSante/nbreOffres*100)

    nbrEnv = Offre.query.filter(Offre.secteur.like("%Agriculture%")).filter(Offre.intitule.like("%"+request.form.get('intitule')+"%")).count()
    pourcentageEnv = round(nbrEnv/nbreOffres*100)

    return render_template("dashboard/rechercheInt.html",offres=offres_list,no=nbOffres,np=nbrePays,ns=ns,cdi=pourcentageCDI,cdd=pourcentageCDD,stage=pourcentageStage,alternance=pourcentageAlternance,freelance=pourcentageFreelance,inf=pourcentageInf,vente=pourcentageVente,batiment=pourcentageBatiment,industrie=pourcentageInd,sante=pourcentageSante,env=pourcentageEnv,pays=pays,recherche=request.form.get('intitule'))
