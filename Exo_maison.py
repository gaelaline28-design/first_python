# Faire un programme, qui récupère l'année de naissance d'un utilisateur et son prenons 
# faites un print dynamique avec la phrase : " bonjour PRENOM, vous avez aujourdhui AGE

# récupération du prénom:
Anaissance = 120
Prenom = input("Quel est ton prénom ? ")

# récupération de l'année de naissance et année actuelle :
Anaissance = int (input("Quelle est ton année de naissance ? "))
Apresent = int (input("Quelle est l'année actuelle ? "))

# calcul de l'âge:
Age = Apresent - Anaissance

# affichage du message:
print(f"Bonjour {Prenom}, vous avez aujourd'hui {Age} ans.")