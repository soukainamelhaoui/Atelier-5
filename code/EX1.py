# Creation de la classe Vecteur2D
class Vecteur2D:
    # Constructeur
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # Methode qui retourne la valeur x
    def get_x(self):
        return self.x
    # Methode qui retourne la valeur 
    def get_y(self):
        return self.y

# Creation des instances 
v1 = Vecteur2D()
v2 = Vecteur2D(3, -7)

# Affichage
print('Le premier vecteur: (', v1.get_x(), ',', v1.get_y(), ')')
print('Le deuxieme vecteur: (', v2.get_x(), ',', v2.get_y(), ')')

