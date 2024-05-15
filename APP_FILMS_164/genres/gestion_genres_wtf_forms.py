"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    identifiant_regexp = r'^[a-zA-Z0-9]+$'
    identifiant_wtf = StringField("Identifiant", validators=[Length(min=2, max=50, message="min 2 max 20"),
                                             Regexp(identifiant_regexp,
                                                    message="pas de caractères "
                                                            "spéciaux, "
                                                            "pas d'espace")
                                             ])

    mdp_regexp = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    mdp_wtf = StringField("mot de passe", validators=[Length(min=8, max=30, message="min 2 max 20"),
                                             Regexp(mdp_regexp,
                                                    message="Il faut au minimum : "
                                                            "1 lettre minuscule "
                                                            "1 lettre majuscule "
                                                            "1 chiffre "
                                                            "1 caractère spécial"
                                                            "Minimum 8 caractère")
                                             ])


    nom_regexp = "^[a-zA-ZÀ-ÿ]+([-']?[a-zA-ZÀ-ÿ]+)*$"
    nom_wtf = StringField("Nom", validators=[Length(min=2, max=50, message="min 2 max 20"),
                                                                   Regexp(nom_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    '''Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
            Définition d'un "bouton" submit avec un libellé personnalisé.
        """ '''

    prenom_regexp = "^[a-zA-ZÀ-ÿ]+([-']?[a-zA-ZÀ-ÿ]+)*$"
    prenom_wtf = StringField("Prénom", validators=[Length(min=2, max=50, message="min 2 max 20"),
                                                         Regexp(prenom_regexp,
                                                                message="Pas de chiffres, de caractères "
                                                                        "spéciaux, "
                                                                        "d'espace à double, de double "
                                                                        "apostrophe, de double trait union")
                                                         ])

    mail_regexp = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    mail_wtf = StringField("mail", validators=[Length(min=4, max=320, message="min 2 max 50"),
                                                         Regexp(mail_regexp,
                                                                message="Pas de chiffres, de caractères "
                                                                        "spéciaux, "
                                                                        "d'espace à double, de double "
                                                                        "apostrophe, de double trait union")
                                                         ])

    num_tel_regexp = "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
    num_tel_wtf = StringField("numéro de téléphone", validators=[Length(min=2, max=50, message="min 2 max 20"),
                                                         Regexp(num_tel_regexp,
                                                                message="Pas de lettre")
                                                         ])


    submit = SubmitField("Enregistrer")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    identifiant_update_regexp = r'^[a-zA-Z0-9]+$'
    identifiant_update_wtf = StringField("Modifier les éléments ", validators=[Length(min=2, max=50, message="min 2 max 20"),
                                                                       Regexp(identifiant_update_regexp,
                                                                              message="pas de caractères "
                                                                                      "spéciaux, "
                                                                                      "pas d'espace")
                                                                       ])
    mdp_update_regexp = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    mdp_update_wtf = StringField("Modifier les éléments ", validators=[Length(min=2, max=30, message="min 2 max 20"),
                                                                       Regexp(mdp_update_regexp,
                                                                              message="Il faut au minimum : "
                                                                                        "1 lettre minuscule "
                                                                                        "1 lettre majuscule "
                                                                                        "1 chiffre "
                                                                                        "1 caractère spécial"
                                                                                        "Minimum 8 caractère")
                                                                       ])

    nom_update_regexp = "^[a-zA-ZÀ-ÿ]+([-']?[a-zA-ZÀ-ÿ]+)*$"
    nom_update_wtf = StringField("Modifier les éléments ", validators=[Length(min=2, max=50, message="min 2 max 20"),
                                                                       Regexp(nom_update_regexp,
                                                                              message="Pas de chiffres, de "
                                                                                      "caractères "
                                                                                      "spéciaux, "
                                                                                      "d'espace à double, de double "
                                                                                      "apostrophe, de double trait "
                                                                                      "union")
                                                                       ])

    prenom_update_regexp = "^[a-zA-ZÀ-ÿ]+([-']?[a-zA-ZÀ-ÿ]+)*$"
    prenom_update_wtf = StringField("Modifier les éléments ", validators=[Length(min=2, max=50, message="min 2 max 20"),
                                                                          Regexp(prenom_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    mail_update_regexp = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    mail_update_wtf = StringField("Modifier les éléments ", validators=[Length(min=4, max=320, message="min 2 max 20"),
                                                                       Regexp(mail_update_regexp,
                                                                              message="Pas de chiffres, de "
                                                                                      "caractères "
                                                                                      "spéciaux, "
                                                                                      "d'espace à double, de double "
                                                                                      "apostrophe, de double trait "
                                                                                      "union")
                                                                       ])

    num_tel_update_regexp = "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
    num_tel_update_wtf = StringField("Modifier les éléments ", validators=[Length(min=9, max=50, message="min 2 max 20"),
                                                                       Regexp(num_tel_update_regexp,
                                                                              message="Pas de lettre")
                                                                       ])

    date_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                               DataRequired("Date non valide")])
    submit = SubmitField("Enregistrer")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_delete_wtf = StringField("Effacer ce genre")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
