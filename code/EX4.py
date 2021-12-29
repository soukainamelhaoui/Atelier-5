# Creation de la classe Point
class Point:
    #  Le constructeur
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def display(self):
        return self.x, self.y

# Creation de la classe Segment
class Segment:
    # Le constructeur
    def __init__(self, xo, yo, xe, ye):
        self.xo = xo
        self.yo = yo
        self.xe = xe
        self.ye = ye
        # Creation des instances de la classe Point
        self.orig = Point(self.xo, self.yo)
        self.extrem = Point(self.xe, self.ye)
    # Methodes d'affichage
    def afficher_orig(self):
        return self.orig.display()

    def afficher_extrem(self):
        return self.extrem.display()

# L'auto-test
seg = Segment(1, 2, 3, 4)
print("Le segmant a les coordonnees", seg.afficher_orig(), "a l'origine, et", seg.afficher_extrem(), "a l'extrimite")

