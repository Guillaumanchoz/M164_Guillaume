"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, PasswordField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp



class FormWTFAjouterGenres(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    identifiant_regexp = r'^[a-zA-Z0-9]+$'
    identifiant_wtf = StringField("Identifiant", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                             Regexp(identifiant_regexp,
                                                    message="pas de caractères "
                                                            "spéciaux, "
                                                            "pas d'espace")
                                             ])

    mdp_regexp = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    mdp_wtf = StringField("mot de passe", validators=[Length(min=8, max=30, message="min 8 max 30"),
                                             Regexp(mdp_regexp,
                                                    message="Il faut au minimum : "
                                                            "1 lettre minuscule "
                                                            "1 lettre majuscule "
                                                            "1 chiffre "
                                                            "1 caractère spécial"
                                                            "Minimum 8 caractère")
                                             ])


    nom_regexp = "^[a-zA-ZÀ-ÿ]+([-']?[a-zA-ZÀ-ÿ]+)*$"
    nom_wtf = StringField("Nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_regexp,
                                                                          message="Pas de chiffres, de caractères spéciaux, "
                                                                                  "d'espace à double, de double apostrophe, de double trait union")
                                                                   ])



    prenom_regexp = "^[a-zA-ZÀ-ÿ]+([-']?[a-zA-ZÀ-ÿ]+)*$"
    prenom_wtf = StringField("Prénom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                         Regexp(prenom_regexp,
                                                                message="Pas de chiffres, de caractères spéciaux, "
                                                                        "d'espace à double, de double apostrophe, de double trait union")
                                                         ])

    mail_regexp = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"
    mail_wtf = StringField("mail", validators=[Length(min=4, max=320, message="min 2 max 50"),
                                                         Regexp(mail_regexp,
                                                                message="Exemple attendu -> test.test@gmail.com "
                                                                "Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")
                                                         ])

    num_tel_regexp = "^0[1-9][0-9](\.\d{3})(\.\d{2}){2}$"
    num_tel_wtf = StringField("numéro de téléphone", validators=[Length(min=13, max=13, message="min 2 max 20"),
                                                         Regexp(num_tel_regexp,
                                                                message="format à respecter : 076.123.12.12")
                                                         ])


    '''Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
            Définition d'un "bouton" submit avec un libellé personnalisé.
        """ '''


    submit = SubmitField("Enregistrer le compte")
    submit_btn_annuler = SubmitField("Annuler")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    identifiant_compte_regexp = r'^[a-zA-Z0-9]+$'
    identifiant_compte_wtf = StringField("identifiant ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                       Regexp(identifiant_compte_regexp,
                                                                              message="pas de caractères "
                                                                                      "spéciaux, "
                                                                                      "pas d'espace")
                                                                       ])

    mdp_regexp = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    mdp_wtf = StringField("mot de passe ", validators=[Length(min=2, max=30, message="min 2 max 20"),
                                                       Regexp(mdp_regexp,
                                                              message="Il faut au minimum : "
                                                                      "1 lettre minuscule "
                                                                      "1 lettre majuscule "
                                                                      "1 chiffre "
                                                                      "1 caractère spécial"
                                                                      "Minimum 8 caractère")
                                                       ])
    nom_regexp = "^[a-zA-ZÀ-ÿ]+([-']?[a-zA-ZÀ-ÿ]+)*$"
    nom_wtf = StringField("nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                       Regexp(nom_regexp,
                                                                              message="Pas de chiffres, de caractères spéciaux, "
                                                                                      "d'espace à double, de double apostrophe, de double trait union")
                                                                       ])

    prenom_regexp = "^[a-zA-ZÀ-ÿ]+([-']?[a-zA-ZÀ-ÿ]+)*$"
    prenom_wtf = StringField("prénom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(prenom_regexp,
                                                                                 message="Pas de chiffres, de caractères spéciaux, "
                                                                                         "d'espace à double, de double apostrophe, de double trait union")
                                                                          ])

    mail_regexp = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"
    mail_wtf = StringField("mail", validators=[Length(min=4, max=320, message="min 2 max 320"),
                                                                       Regexp(mail_regexp,
                                                                              message="Exemple attendu -> test.test@gmail.com "
                                                                              "Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")
                                                                       ])

    num_tel_regexp = "^0[1-9][0-9](\.\d{3})(\.\d{2}){2}$"
    num_tel_wtf = StringField("numéro de téléphone ", validators=[Length(min=9, max=50, message="min 2 max 20"),
                                                                       Regexp(num_tel_regexp,
                                                                              message="format à respecter : 076.123.12.12")
                                                                       ])


    date_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                               DataRequired("Date non valide")])
    submit = SubmitField("Enregistrer")
    submit_btn_annuler = SubmitField("Annuler")




class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    Identifiant_delete_wtf = StringField("Identifiant")
    password = PasswordField('Mot de passe')
    nom_delete_wtf = StringField("Nom")
    prenom_delete_wtf = StringField("Prénom")
    mail_delete_wtf = StringField("Mail")
    num_tel_delete_wtf = StringField("Numéro de téléphone")
    designation_delete_wtf = StringField("Statut du compte")

    submit_btn_del = SubmitField("Effacer")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")