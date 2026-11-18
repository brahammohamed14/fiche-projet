taches = []

while True:
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Titre de la tâche : ")

        if titre.strip() != "":
            taches.append(titre)
            print("Tâche ajoutée avec succès.")
        else:
            print("Erreur : le titre ne peut pas être vide.")
    elif choix == "2":
        if len(taches) == 0:
            print("Aucune tâche enregistrée.")
        else:
            print("\nListe des tâches :")
            for i, tache in enumerate(taches, start=1):
                print(f"{i}. {tache}")

    elif choix == "3":
        mot_cle = input("Mot-clé à rechercher : ")
        trouve = False

        for i, tache in enumerate(taches, start=1):
            if mot_cle.lower() in tache.lower():
                print(f"{i}. {tache}")
                trouve = True

        if not trouve:
            print("Aucune tâche trouvée.")        

    elif choix == "0":
        print("vous quittez !")
        break

    else:
        print("Option non disponible pour le moment.")
