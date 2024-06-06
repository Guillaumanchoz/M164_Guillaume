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
                compte_id = 0


                valeurs_insertion_dictionnaire = {"value_statut": statut,
                                                  "value_user": username,
                                                  "value_mdp": password,
                                                  "value_heure": heure,
                                                  "value_date": date,
                                                  "value_nombre": nombre,
                                                  "value_compte_id": compte_id,
                                                  }
                date_creation = datetime.today().strftime("%Y-%m-%d")
                print("ICI?")
                #requete
                strsql_get_password = """SELECT Mot_de_passe FROM t_compte WHERE Identifiant_compte = %(value_user)s"""
                strsql_compte_id = """SELECT ID_compte FROM t_compte WHERE Identifiant_compte = %(value_user)s"""
                strsql_check_reservation = """SELECT COUNT(*) FROM t_reservation WHERE FK_heure = %(value_heure)s AND date = %(value_date)s"""
                strsql_reservation = """INSERT INTO t_reservation (id_reservation, FK_statut_res, FK_compte, FK_heure, date, nombre, date_creation) VALUES (NULL, %(value_statut)s, %(value_compte_id)s, %(value_heure)s, %(value_date)s, %(value_nombre)s, %(date_creation)s) """


                valeurs_insertion_dictionnaire["date_creation"] = date_creation

                with DBconnection() as mconn_bd:

                    mconn_bd.execute(strsql_get_password, valeurs_insertion_dictionnaire)
                    check_mdp_dict = mconn_bd.fetchone()
                    check_mdp = check_mdp_dict.get("Mot_de_passe")
                    print("ICI?")
                    if password == check_mdp:
                        mconn_bd.execute(strsql_compte_id, valeurs_insertion_dictionnaire)
                        check_compte_dict = mconn_bd.fetchone()
                        check_compte = check_compte_dict.get("ID_compte")

                        valeurs_insertion_dictionnaire["value_compte_id"] = check_compte

                        ## Vérification de l'existence d'une réservation à la même heure et le même jour
                        mconn_bd.execute(strsql_check_reservation, valeurs_insertion_dictionnaire)
                        count_reservation = mconn_bd.fetchone()['COUNT(*)']

                        if count_reservation > 0:
                            flash("Une réservation existe déjà à cette heure et ce jour.", "danger")
                        else:
                            mconn_bd.execute(strsql_reservation, valeurs_insertion_dictionnaire)
                            flash(f"Données insérées !!", "success")

                            # Pour afficher et constater l'insertion du nouveau film (id_film_sel=0 => afficher tous les films)
                            return redirect(url_for('reservation_afficher', id_film_sel=0))

                    else:
                        flash("Identifiant ou Mot de passe incorrect", "danger")

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

@app.route("/id_reservation_update", methods=['GET', 'POST'])
def film_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_film"
    id_reservation_update = request.values['id_film_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_film = FormWTFUpdateFilm()
    try:
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update_film.submit.data:

            statut = 1
            username = form_update_film.username.data
            password = form_update_film.password.data
            heure = form_update_film.heure_update_wtf.data
            date = form_update_film.date_update_wtf.data
            nombre = form_update_film.nombre_update_wtf.data

            #rentrer les valeurs dans le dictionnaire
            valeur_update_dictionnaire = {"value_id_reservation": id_reservation_update,
                                          "value_statut": statut,
                                              "value_user": username,
                                              "value_mdp": password,
                                              "value_heure": heure,
                                              "value_date": date,
                                              "value_nombre": nombre,
                                              }

            date_creation = datetime.today().strftime("%Y-%m-%d")

            #requete
            strsql_get_password = """SELECT Mot_de_passe FROM t_compte WHERE Identifiant_compte = %(value_user)s"""
            strsql_check_reservation_update = """SELECT COUNT(*) FROM t_reservation WHERE FK_heure = %(value_heure)s AND date = %(value_date)s"""
            strsql_id_reservation_check = """SELECT ID_reservation FROM t_reservation WHERE FK_heure = %(value_heure)s AND date = %(value_date)s"""

            strsql_update_reservation = """UPDATE t_reservation SET FK_statut_res = %(value_statut)s,
                                                                    FK_heure = %(value_heure)s,
                                                                    date = %(value_date)s,
                                                                    nombre = %(value_nombre)s,
                                                                    date_creation = %(date_creation)s
                                                                    WHERE id_reservation = %(value_id_reservation)s"""

            strsql_update_reservation_egale = """UPDATE t_reservation SET   FK_statut_res = %(value_statut)s,
                                                                            nombre = %(value_nombre)s,
                                                                            date_creation = %(date_creation)s
                                                                            WHERE id_reservation = %(value_id_reservation)s"""



            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            valeur_update_dictionnaire["date_creation"] = date_creation
            with DBconnection() as mconn_bd:

                mconn_bd.execute(strsql_id_reservation_check, valeur_update_dictionnaire)
                check_id_reservation = mconn_bd.fetchone()
                if check_id_reservation is not None:
                    check_id_res = check_id_reservation.get("ID_reservation")

                    #Si garde la même heure et le même jour.
                    if id_reservation_update == str(check_id_res):

                        mconn_bd.execute(strsql_get_password, valeur_update_dictionnaire)
                        check_mdp_dict = mconn_bd.fetchone()
                        check_mdp = check_mdp_dict.get("Mot_de_passe")

                        if password == check_mdp:
                            mconn_bd.execute(strsql_update_reservation_egale, valeur_update_dictionnaire)
                            flash(f"Données insérées !!", "success")

                            # Pour afficher et constater l'insertion du nouveau film (id_film_sel=0 => afficher tous les films)
                            return redirect(url_for('reservation_afficher', id_film_sel=0))
                        else :
                            flash("Erreur de mot de passe.", "danger")

                    #Sinon c'est que c'est une réservation déjà prise.
                    else:
                        mconn_bd.execute(strsql_check_reservation_update, valeur_update_dictionnaire)
                        count_reservation = mconn_bd.fetchone()['COUNT(*)']

                        if count_reservation > 0:
                            flash("Une réservation existe déjà à cette heure pour ce jour.", "danger")
                            return redirect(url_for('reservation_afficher', id_film_sel=id_reservation_update))

                #si change le jour ou l'heure
                else :
                    mconn_bd.execute(strsql_get_password, valeur_update_dictionnaire)
                    check_mdp_dict = mconn_bd.fetchone()
                    check_mdp = check_mdp_dict.get("Mot_de_passe")

                    if password == check_mdp:
                        mconn_bd.execute(strsql_update_reservation, valeur_update_dictionnaire)
                        flash(f"Données insérées !!", "success")
                    else:
                        flash("Erreur de mot de passe.", "danger")



            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_reservation_update"
            return redirect(url_for('reservation_afficher', id_film_sel=id_reservation_update))

        elif request.method == "GET":
            # requete
            strsql_id_reservation = """SELECT ID_reservation, Identifiant_compte, Mot_de_passe, FK_heure, date, nombre FROM t_reservation r
                                        INNER JOIN t_compte c ON c.id_compte = r.FK_compte
                                        INNER JOIN t_statut_res s ON s.id_statut_res = r.FK_statut_res
                                        WHERE ID_reservation = %(value_id_reservation)s """
            valeur_select_dictionnaire = {"value_id_reservation": id_reservation_update}

            print("valeur_select_dictionnaire ", valeur_select_dictionnaire)

            with DBconnection() as mybd_conn:
                mybd_conn.execute(strsql_id_reservation, valeur_select_dictionnaire)
                data_reservation = mybd_conn.fetchone()
                print("ouiuiiiii")

            form_update_film.username.data = data_reservation["Identifiant_compte"]
            form_update_film.password.data = data_reservation["Mot_de_passe"]
            form_update_film.date_update_wtf.data = data_reservation["date"]
            form_update_film.heure_update_wtf.data = str(data_reservation["FK_heure"])
            form_update_film.nombre_update_wtf.data = data_reservation["nombre"]

            print(f"valeur_data_reservation : {data_reservation}")

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
            return redirect(url_for("reservation_afficher", id_film_sel=0))

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
            return redirect(url_for('reservation_afficher', id_film_sel=0))
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
