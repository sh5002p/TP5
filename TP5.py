def input_nom_prenom():
    noms = []
    prenoms = []

    for i in range(2):
        nom = input(f"Entrez le nom {i+1} : ")
        noms.append(nom.upper())

        prenom = input(f"Entrez le prénom {i+1} : ")
        prenoms.append(prenom.capitalize())

    return noms, prenoms

def affiche_resultat(noms, prenoms):
    noms_prenoms = list(zip(noms, prenoms))
    noms_prenoms.sort()

    for nom, prenom in noms_prenoms:
        print(f"{prenom} {nom}")

if __name__ == "__main__":
    noms, prenoms = input_nom_prenom()
    affiche_resultat(noms, prenoms)

ex2:
def input_notes_coefficients():
    notes = []
    coefficients = []

    for i in range(5):
        print(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant :")
        input_data = input().split(" ")

        notes.append(float(input_data[0]))
        coefficients.append(int(input_data[1]))

    return notes, coefficients

def calcul_moyenne_generale(notes, coefficients):
    return sum(note * coefficient for note, coefficient in zip(notes, coefficients)) / sum(coefficients)

def evaluer_admission(moyenne_generale, notes):
    return moyenne_generale > 10 and all(note >= 8 for note in notes)

if __name__ == "__main__":
    notes, coefficients = input_notes_coefficients()
    moyenne_generale = calcul_moyenne_generale(notes, coefficients)
    admis = evaluer_admission(moyenne_generale, notes)

    print(f"La moyenne générale de l'étudiant est de {moyenne_generale}")

    if admis:
        print("L'étudiant est admis.")
    else:
        print("L'étudiant n'est pas admis.")

ex3 :
def est_palindrome(chaine):
    chaine = chaine.lower()
    chaine = ''.join(c for c in chaine if c.isalpha())
    return chaine == chaine[::-1]

if __name__ == "__main__":
    chaine = input("Entrez un mot ou une phrase : ")
    if est_palindrome(chaine):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

ex4 :


def somme_en_billets_et_pieces(somme):
    denominations = [100, 50, 10, 2, 1]
    resultat = {}

    for denomination in denominations:
        nombre_billets_ou_pieces = somme // denomination
        somme -= nombre_billets_ou_pieces * denomination
        resultat[denomination] = nombre_billets_ou_pieces

    return resultat


if __name__ == "__main__":
    somme = int(input("Entrez une somme en euros : "))
    resultat = somme_en_billets_et_pieces(somme)

    print(f"{somme} euros, c’est donc {resultat[100]} billets de 100,", end=' ')
    print(f"{resultat[50]} de 50, {resultat[10]} de 10,", end=' ')
    print(f"{resultat[2]} pièces de 2 et {resultat[1]} pièce 1.")

ex 5 :

def calculer_salaire(heures_travaillées, salaire_horaire):
    salaire_base = min(heures_travaillées, 160) * salaire_horaire
    heures_a_majorer = max(0, heures_travaillées - 160)
    majoration_25pc = heures_a_majorer * salaire_horaire * 1.25
    majoration_50pc = max(0, heures_a_majorer - 40) * salaire_horaire * 1.5
    salaire_total = salaire_base + majoration_25pc + majoration_50pc
    return salaire_total

if __name__ == "__main__":
    heures_travaillées = int(input("Entrez le nombre d'heures travaillées : "))
    salaire_horaire = float(input("Entrez le salaire horaire : "))
    salaire_total = calculer_salaire(heures_travaillées, salaire_horaire)
    print(f"Le salaire total est de {salaire_total} euros.")

ex6 :


def calculer_taille(chaine):
    return len(chaine)


def calculer_pourcentage_voyelles(chaine):
    voyelles = 'aeiouAEIOU'
    nombre_voyelles = 0
    for char in chaine:
        if char in voyelles:
            nombre_voyelles += 1
    return (nombre_voyelles / len(chaine)) * 100


def est_sous_chaine(chaine, sous_chaine):
    debut = chaine.find(sous_chaine)
    if debut != -1:
        return debut
    else:
        return False


def calculer_nombre_occurrences(chaine, sous_chaine):
    return chaine.count(sous_chaine)


if __name__ == "__main__":
    chaine = input("Entrez une chaîne de caractères : ")
    taille = calculer_taille(chaine)
    pourcentage_voyelles = calculer_pourcentage_voyelles(chaine)
    est_wagon_sous_chaine = est_sous_chaine(chaine, 'wagon')
    nombre_occurrences_wagon = calculer_nombre_occurrences(chaine, 'wagon')

    print(f"La taille de la chaîne est de {taille} caractères.")
    print(f"Le pourcentage de voyelles est de {pourcentage_voyelles}%.")

    if est_wagon_sous_chaine:
        print(f"La chaîne 'wagon' est une sous-chaîne de la chaîne et commence à l'index {est_wagon_sous_chaine}.")
    else:
        print("La chaîne 'wagon' n'est pas une sous-chaîne de la chaîne.")

    print(f"Le nombre d'occurrences de la chaîne 'wagon' est de {nombre_occurrences_wagon}.")

ex 7 :

import os
import datetime

def afficher_info_fichier(nom_fichier):
    if os.path.isfile(nom_fichier):
        taille_octets = os.path.getsize(nom_fichier)
        date_modif = os.path.getmtime(nom_fichier)
        date_formatee = datetime.datetime.fromtimestamp(date_modif).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Le fichier {nom_fichier} existe. Sa taille est de {taille_octets} octets et il a été modifié pour la dernière fois le {date_formatee}.")
    else:
        print(f"Le fichier {nom_fichier} n'existe pas.")

if __name__ == "__main__":
    nom_fichier1 = input("Entrez le nom du premier fichier : ")
    nom_fichier2 = input("Entrez le nom du deuxième fichier : ")

    afficher_info_fichier(nom_fichier1)
    afficher_info_fichier(nom_fichier2)

    if os.path.isfile(nom_fichier1) and os.path.isfile(nom_fichier2):
        date_modif1 = os.path.getmtime(nom_fichier1)
        date_modif2 = os.path.getmtime(nom_fichier2)

        if date_modif1 > date_modif2:
            print(f"Le fichier {nom_fichier1} est le plus récent.")
        elif date_modif1 < date_modif2:
            print(f"Le fichier {nom_fichier2} est le plus récent.")
        else:
            print("Les deux fichiers ont été modifiés en même temps.")
    else:
        print("L'un des fichiers n'existe pas, impossible de déterminer le plus récent.")
