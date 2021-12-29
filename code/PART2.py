# Creation de la classe Etudiant
class Etudiant:
    # Constructeur
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
    # Methode pour retourner le noms complet d'etudiant
    def __repr__(self):
        nomComplet = self.nom + " " + self.prenom
        return nomComplet
    

# Creation d'une liste des instances etudiants
listeEtu = [ Etudiant("Alaoui", "Amine", 19, "H4576909", 15),
             Etudiant("Zrek", "Karima", 21, "F7843324", 13),
             Etudiant("Ezzalz", "Abdo", 19, "G1779045", 16.5)]

# Ordonner la liste selon l'age
listeEtu.sort(key=lambda item:item.age, reverse=True)
print('Les etudiants ordonnes selon leurs ages:', listeEtu.__repr__())

# Ordonner la liste selon la moyenne
listeEtu.sort(key=lambda item:item.moyenne, reverse=True)
print('Les etudiants ordonnes selon la moyennes:', listeEtu.__repr__())



