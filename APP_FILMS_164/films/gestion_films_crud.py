"""Gestion des "routes" FLASK et des données pour les films.
Fichier : gestion_films_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from datetime import datetime
import pymysql.cursors

from flask import redirect
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.films.gestion_films_wtf_forms import FormWTFUpdateFilm, FormWTFAddFilm, FormWTFDeleteFilm

"""Ajouter un film grâce au formulaire "film_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "films/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/film_add", methods=['GET', 'POST'])
def film_add_wtf():
    # Objet formulaire pour AJOUTER un film
    form_add_film = FormWTFAddFilm()
    if request.method == "POST":
        try:
            if form_add_film.validate_on_submit():

                statut = 1
                username = form_add_film.username.data
                password = form_add_film.password.data
                heure = form_add_film.heure_add_wtf.data
                date = form_add_film.date_add_wtf.data
                nombre = form_add_film.nombre_add_wtf.data
                id_heure = 0
                compte_id = 0

                valeurs_insertion_dictionnaire = {"value_statut": statut,
                                                  "value_user": username,
                                                  "value_mdp": password,
                                                  "value_heure": heure,
                                                  "value_date": date,
                                                  "value_nombre": nombre,
                                                  "value_id_heure": id_heure,
                                                  "value_compte_id": compte_id
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)


                strsql_get_password = """SELECT Mot_de_passe FROM t_compte WHERE Identifiant_compte = %(value_user)s"""
                strsql_compte_id = """SELECT ID_compte FROM t_compte WHERE Identifiant_compte = %(value_user)s"""
                strsql_id_heure = """SELECT ID_heure FROM t_heure WHERE heure = %(value_heure)s """

                date = datetime.today().strftime("%Y-%m-%d")

                strsql_reservation = """INSERT INTO t_reservation (id_reservation, FK_statut_res, FK_compte, FK_heure, date, nombre, date_creation) VALUES (NULL, %(value_statut)s, %(value_compte_id)s, %(value_id_heure)s, %(value_date)s, %(value_nombre)s, %(date_creation)s) """

                valeurs_insertion_dictionnaire["date_creation"] = date

                with DBconnection() as mconn_bd:

                    mconn_bd.execute(strsql_get_password, valeurs_insertion_dictionnaire)
                    check_mdp_dict = mconn_bd.fetchone()
                    check_mdp = check_mdp_dict.get("Mot_de_passe")

                    print(f"pwd: {password} / check_mdp: {check_mdp}")

                    if password == check_mdp:
                        mconn_bd.execute(strsql_compte_id, valeurs_insertion_dictionnaire)
                        check_compte_dict = mconn_bd.fetchone()
                        check_compte = check_compte_dict.get("ID_compte")

                        print(f"check_compte : {check_compte}")
                        valeurs_insertion_dictionnaire["value_compte_id"] = check_compte

                        # Récupérer l'ID de l'heure à partir de la base de données
                        mconn_bd.execute(strsql_id_heure, valeurs_insertion_dictionnaire)
                        check_heure_dict = mconn_bd.fetchone()
                        check_heure = check_heure_dict.get("ID_heure")

                        print(f"heure : {heure} / heureid : {check_heure}")
                        valeurs_insertion_dictionnaire["value_id_heure"] = check_heure


                        mconn_bd.execute(strsql_reservation, valeurs_insertion_dictionnaire)

                        flash(f"Données insérées !!", "success")
                        print(f"Données insérées !!")

                        # Pour afficher et constater l'insertion du nouveau film (id_reservation_sel=0 => afficher tous les films)
                        return redirect(url_for('reservation_afficher', id_reservation_sel=0))

                    else:
                        flash("Aucun mot de passe trouvé pour cet utilisateur.", "danger")
                        flash("Mot de passe incorrect", "danger")
                        flash("Aucune heure correspondante trouvée dans la base de données.", "danger")

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{film_add_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("films/film_add_wtf.html", form_add_film=form_add_film)










"""Editer(update) un film qui a été sélectionné dans le formulaire "reservation_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"

Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "films/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/film_update", methods=['GET', 'POST'])
def film_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_film"
    id_film_update = request.values['id_film_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_film = FormWTFUpdateFilm()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update_film.submit.data:

            statut = 1
            username = form_update_film.username.data
            password = form_update_film.password.data
            heure = form_update_film.heure_add_wtf.data
            date = form_update_film.date_add_wtf.data
            nombre = form_update_film.nombre_add_wtf.data
            id_heure = 0
            compte_id = 0

            valeur_update_dictionnaire = {"value_statut": statut,
                                                  "value_user": username,
                                                  "value_mdp": password,
                                                  "value_heure": heure,
                                                  "value_date": date,
                                                  "value_nombre": nombre,
                                                  "value_id_heure": id_heure,
                                                  "value_compte_id": compte_id
                                                  }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_film = """UPDATE t_reservation SET FK_statut-res = %(value_statut)s,
                                                            FK_compte = %(value_id_heure)s,
                                                            FK_heure = %(value_description_film)s,
                                                            date = %(value_date)s,
                                                            nombre = %(value_nombre)s, 
                                                            date_creation = %(date_creation)s
                                                            WHERE id_film = %(value_id_film)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_film, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_film_update"
            return redirect(url_for('reservation_afficher', id_reservation_sel=id_film_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_film" et "intitule_genre" de la "t_genre"
            str_sql_id_film = "SELECT * FROM t_film WHERE id_film = %(value_id_film)s"
            valeur_select_dictionnaire = {"value_id_film": id_film_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_film, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_film = mybd_conn.fetchone()
            print("data_film ", data_film, " type ", type(data_film), " genre ",
                  data_film["nom_film"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "film_update_wtf.html"
            form_update_film.nom_film_update_wtf.data = data_film["nom_film"]
            form_update_film.duree_film_update_wtf.data = data_film["duree_film"]
            # Debug simple pour contrôler la valeur dans la console "run" de PyCharm
            print(f" duree film  ", data_film["duree_film"], "  type ", type(data_film["duree_film"]))
            form_update_film.description_film_update_wtf.data = data_film["description_film"]
            form_update_film.cover_link_film_update_wtf.data = data_film["cover_link_film"]
            form_update_film.datesortie_film_update_wtf.data = data_film["date_sortie_film"]

    except Exception as Exception_film_update_wtf:
        raise ExceptionFilmUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_update_wtf.__name__} ; "
                                     f"{Exception_film_update_wtf}")

    return render_template("films/film_update_wtf.html", form_update_film=form_update_film)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "reservation_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_film_delete_wtf" du formulaire "films/film_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/film_delete", methods=['GET', 'POST'])
def film_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_film_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_film"
    id_film_delete = request.values['id_film_btn_delete_html']

    # Objet formulaire pour effacer le film sélectionné.
    form_delete_film = FormWTFDeleteFilm()
    try:
        # Si on clique sur "ANNULER", afficher tous les films.
        if form_delete_film.submit_btn_annuler.data:
            return redirect(url_for("reservation_afficher", id_reservation_sel=0))

        if form_delete_film.submit_btn_conf_del_film.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "films/film_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_film_delete = session['data_film_delete']
            print("data_film_delete ", data_film_delete)

            flash(f"Effacer le film de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_film.submit_btn_del_film.data:
            valeur_delete_dictionnaire = {"value_id_film": id_film_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_film_genre = """DELETE FROM t_genre_film WHERE fk_film = %(value_id_film)s"""
            str_sql_delete_film = """DELETE FROM t_film WHERE id_film = %(value_id_film)s"""
            # Manière brutale d'effacer d'abord la "fk_film", même si elle n'existe pas dans la "t_genre_film"
            # Ensuite on peut effacer le film vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_film_genre, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_film, valeur_delete_dictionnaire)

            flash(f"Film définitivement effacé !!", "success")
            print(f"Film définitivement effacé !!")

            # afficher les données
            return redirect(url_for('reservation_afficher', id_reservation_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_film": id_film_delete}
            print(id_film_delete, type(id_film_delete))

            # Requête qui affiche le film qui doit être efffacé.
            str_sql_genres_films_delete = """SELECT * FROM t_film WHERE id_film = %(value_id_film)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_film_delete = mydb_conn.fetchall()
                print("data_film_delete...", data_film_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "films/film_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_film_delete'] = data_film_delete

            # Le bouton pour l'action "DELETE" dans le form. "film_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_film_delete_wtf:
        raise ExceptionFilmDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_delete_wtf.__name__} ; "
                                     f"{Exception_film_delete_wtf}")

    return render_template("films/film_delete_wtf.html",
                           form_delete_film=form_delete_film,
                           btn_submit_del=btn_submit_del,
                           data_film_del=data_film_delete
                           )
