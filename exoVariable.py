# -------------- exo 1 --------------
# Print une phrase dynamique (dynamique - avec des données changeante) 
# "je suis PRENOM, j"habite a VILLE et j'ai AGE" 
# prenom, ville et age seront dans des variables

#variables
Prenom = "gaël"
City = "Cenon"
Age = 0

#affichage
print(f"Je suis {Prenom}, j'habite {City} et j'ai {Age}")


#-------------- exo 2 --------------
# Print une phrase le total est de TOTAL euros 10 
# vous avez acheté une baguette et un croissant 
# le montant de ces articles sont dans des variables

#variables
Baguettes = 0
Croissants = 1
Total= 0

#opération
Total = Baguettes + Croissants

#Affichage
print(f"le total est {Total} €")


#-------------- exo 3 --------------
# Lors d'un jeu vous avez dix points 
#Faire un print de vos points 
# Au premier tour vous perdez 1 pts 
# au deuxieme tour vous en gagnez 5 
# au dernier tour vous en perdez la moitié 
# faire un print de votre nouveau total de points a chaque tours

#variables
txt = "mon nombre de point est de"
Score = 10
Ptour = 1
Dtour = 5

Total = 10
#print(f"mon nombre de point est de {Total}")
print(txt,Total)

#au premier tour on perd 1 point
Total -=Ptour
#print(f"mon nombre de point est de {Total}")
print(txt,Total)

#au 2° tour on gagne 5
Total += Dtour 
#print(f"mon nombre de point est de {Total}")
print(txt,Total)

#au dernier tour un perd la moitier
Total = Total-Total/2 
#print(f"mon nombre de point est de {Total}")
print(txt,Total)
