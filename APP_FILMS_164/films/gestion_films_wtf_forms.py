"""Gestion des formulaires avec WTF pour les films
Fichier : gestion_films_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField, IntegerField, DateField, SelectField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea



class FormWTFAddFilm(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    username = StringField('Identifiant', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired(message="Il manque le mot de passe !!!")])


    date_add_wtf = DateField("Date de la réservation", validators=[InputRequired("Date obligatoire"),
                                                                                 DataRequired("Date non valide")])


    heure_add_wtf = SelectField("heure", choices=[
        (1, "8h00 - 9h45"),
        (2, "10h00 - 11h45"),
        (3, "13h00 - 14h45"),
        (4, "15h00 - 16h45")
    ], validators=[DataRequired()])

    nombre_regexp = "^(?:[1-9]|[1-4][0-9]|50)$"
    nombre_add_wtf = StringField("Nombre ", validators=[Length(min=1, max=50, message="min 1 max 50"),
                                                               Regexp(nombre_regexp,
                                                                      message="uniquement des chiffres entre 1 et 50 ")
                                                               ])

    submit = SubmitField("Reserver")


class FormWTFUpdateFilm(FlaskForm):
    """
        Dans le formulaire "film_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    username = StringField('Identifiant', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired(message="Il manque le mot de passe !!!")])

    date_update_wtf = DateField("Date de la réservation", validators=[InputRequired("Date obligatoire"),
                                                                   DataRequired("Date non valide")])

    nombre_regexp = "^(?:[1-9]|[1-4][0-9]|50)$"
    nombre_update_wtf = StringField("Nombre ", validators=[Length(min=1, max=50, message="min 1 max 50"),
                                                        Regexp(nombre_regexp,
                                                               message="uniquement des chiffres entre 1 et 50 ")
                                                        ])

    heure_update_wtf = SelectField("heure", choices=[
        (1, "8h00 - 9h45"),
        (2, "10h00 - 11h45"),
        (3, "13h00 - 14h45"),
        (4, "15h00 - 16h45")
    ], validators=[DataRequired()])

    submit = SubmitField("Enregistrer")


class FormWTFDeleteFilm(FlaskForm):
    """
        Dans le formulaire "film_delete_wtf.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_film_delete_wtf = StringField("Effacer ce film")
    submit_btn_del_film = SubmitField("Effacer film")
    submit_btn_conf_del_film = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
