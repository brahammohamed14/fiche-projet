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

    elif choix == "0":
        print("vous quittez !")
        break

    else:
        print("Option non disponible pour le moment.")
