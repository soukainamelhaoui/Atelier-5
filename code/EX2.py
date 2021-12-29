# Creation de la classe Vecteur2D
class Vecteur2D:
    # Constructeur
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # Methode d'affichage
    def afficher(self):
        print('Le vecteur est: (', self.x, ',', self.y, ')')
    # Methode d'addition
    def __add__(self, other):
        return self.x + other.x, self.y + other.y

# Creation des instances
v1 = Vecteur2D(2, -2)
v2 = Vecteur2D(1, 6)

# Affichage des vecteurs
v1.afficher()
v2.afficher()

# L'addition
res = v1 + v2
print('Le resultat d\'addition des deux vecteurs:',res)