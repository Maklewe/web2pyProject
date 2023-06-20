def liste():
    rows = db().select(db.reservations.ALL)
    return response.render('reservations/liste.html', dict(reservations=rows))

def ajout():
    affiche = db().select(db.affiches.ALL)
    utilisateur = db().select(db.auth_user.ALL)
    if request.method == 'POST':
        db.reservations.insert(
            nombre_places = request.vars.nombre_places,
            affiche_id = request.vars.affiche_id,
            utilisateur_id = request.vars.utilisateur_id
        )
        print(request.vars.affiche)
        print(request.vars.utilisateur)
        redirect(URL('reservations', 'liste'))
    return response.render('reservations/ajout.html',dict(affiches=affiche, utilisateurs=utilisateur))

def supprimer():
    id = request.vars.id
    db(db.films.id == id).delete()
    redirect(URL('reservations', 'liste'))