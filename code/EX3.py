# Creation de la classe Rectangle
class Rectangle:
    # L'attribut rectangle
    nom = "rectangle"
    # Constructeur par defaut
    def __init__(self):
        self.longuer = 7
        self.largeur = 15
    # Methode d'affichage
    def afficher(self):
        print('Un', self.nom, 'avec une largeur =', self.largeur, ',et longueur =', self.longuer)
    # Methode qui calcul la surface
    def surface(self):
        return self.largeur * self.longuer

# Creaction du sous-classe Carre
class Carre(Rectangle):
    #  Constructeur
    def __init__(self):
        super().__init__()
        self.size = 5
    # Surcharge de l'attribut nom
    nom = 'carre'
    # Methode d'affichage
    def afficher(self):
        print('Un', self.nom, 'avec une taille =', self.size)
    # Methode surface
    def surface(self):
        return self.size * self.size

# Instance de la classe Rectangle
rect = Rectangle()
rect.afficher()
print('La surface du rectangle est:', rect.surface())

# Instance de la classe Carre
carre = Carre()
carre.afficher()
print('La surface du carre est:', carre.surface())