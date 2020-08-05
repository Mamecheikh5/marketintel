# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from dashboard import db, login_manager


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(228))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))



class restaurants(db.Model):
    """
    Create a Restaurant table
    """

    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(60))
    description = db.Column(db.String(200))
    adresse=db.Column(db.String(300))
    pays=db.Column(db.String(200))
    telephone=db.Column(db.String(200))
    region=db.Column(db.String(200))

    def __repr__(self):
        return '<Restaurants: {}>'.format(self.nom)



class Car(db.Model):
    """
    Create a Role table
    """

    _tablename_ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    vendeur = db.Column(db.String(60))
    constructeur=db.Column(db.String(60))
    modele=db.Column(db.String(60))
    kilometrage=db.Column(db.String(60))
    carburant=db.Column(db.String(60))
    annee=db.Column(db.String(60))
    localisation=db.Column(db.String(60))
    contact=db.Column(db.String(60))
    transmission=db.Column(db.String(60))
    prix=db.Column(db.Float)
    vendeur=db.Column(db.String(60))
    
    
    def _repr_(self):
        return '<Car: {}>'.format(self.vendeur)

class Immobilier(db.Model):
    _tablename_ = 'immobilier'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    intitule = db.Column(db.String)
    price = db.Column(db.Integer)
    monnaie = db.Column(db.String)
    seller = db.Column(db.String)
    date = db.Column(db.String)
    surface = db.Column(db.Integer)
    chambre = db.Column(db.Integer)

class Offre(db.Model):

    """
    Create an Offre table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'offres'

    intitule = db.Column(db.Text())
    description = db.Column(db.Text())
    secteur = db.Column(db.Text())
    salaire = db.Column(db.Text())
    typeContrat = db.Column(db.Text())
    experience = db.Column(db.Text())
    niveau = db.Column(db.Text())
    entreprise = db.Column(db.Text())
    lieu = db.Column(db.Text())
    pays = db.Column(db.Text())
    date = db.Column(db.Text())
    lien = db.Column(db.Text(),primary_key=True)

    def __init__(self,intitule,description,secteur,salaire,typeContrat,experience,niveau,entreprise,date,lieu,pays,lien):
        self.intitule = intitule
        self.description = description
        self.secteur = secteur
        self.salaire = salaire
        self.typeContrat = typeContrat
        self.experience = experience
        self.niveau = niveau
        self.entreprise = entreprise
        self.date = date
        self.lieu = lieu
        self.pays = pays
        self.lien = lien

    def __repr__(self):
        return '<lien {}>'.format(self.lien)