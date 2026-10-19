# -------------- exo 1 --------------
#variables
Prenom = "gaël"
City = "Cenon"
Age = 0

#affichage
print(f"Je suis {Prenom}, j'habite {City} et j'ai {Age}")


#-------------- exo 2 --------------
#variables
Baguettes = 0
Croissants = 1
Total= 0

#opération
Total = Baguettes + Croissants

#Affichage
print(f"le total est {Total} €")


#-------------- exo 3 --------------
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
