from math import pi
from math import pow

# PARTIE A

class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def afficher(self):
        print(f"Point({self.x}, {self.y})")


class Cercle():
    def __init__(self, centre, rayon):
        self.centre= centre
        self.rayon=rayon

    def getPerimetre(self):
        return 2*pi*self.rayon

    def getSurface(self):
        return pi*pow(self.rayon, 2)

    def afficher(self):
        print(F"\t\t\tCercle({self.centre.x}, {self.centre.y}, {self.rayon})")

    def appartient(self, p):
        if pow(p.x - self.centre.x, 2) + pow(p.y - self.centre.y, 2) == pow(self.rayon, 2):
            print("\t\t\tCe point appartient au cercle")

        else:
            print("\t\t\tCe point n'appartient pas au cercle")




print("\t------------------------------------------------------------------------------")
print("\t\t\t\t Exercice TP Python")
print("\t------------------------------------------------------------------------------\n")


x=float(input("\t\t\tEntrer l'abscisse du centre: "))
y=float(input("\t\t\tEntrer l'ordonnée du centre: "))
A=Point(x, y)

r=float(input("\t\t\tEntrer le rayon du cercle: "))
C=Cercle(A, r)
print(f"\t\t\tVous avez créé le cercle: ")
C.afficher()
print(f"\t\t\tSon périmètre est: {C.getPerimetre()} m")
print(f"\t\t\tSa surface est: {C.getSurface()} m2")

print("\n\t-------------------------------------------------------------------------------------------")
print("\t\tVérification d'appartenance d'un point quelconque au cercle")
print("\t-------------------------------------------------------------------------------------------\n")
a=float(input("\t\t\tEntrer l'abscisse de ce point: "))
b=float(input("\t\t\tEntrer l'ordonnée de ce point: "))
B=Point(a, b)
C.appartient(B)


# PARTIE B

class Cylindre(Cercle):
    def __init__(self, centre, rayon, hauteur):
        Cercle.__init__(self, centre, rayon)
        self.hauteur=hauteur

    def getVolume(self):
        return pi*pow(self.rayon, 2)*self.hauteur


print("\n\t------------------------------------------------------------------------------")
print("\t\tTenté de transformer ce cercle en Cylindre???")
print("\t------------------------------------------------------------------------------\n")
h=float(input("\t\t\tEh bah donner une hauteur: "))
Cyl=Cylindre(A, r, h)
print(f"\t\t\tLe volume du cylindre obtenu à partir de ce cercle est: {Cyl.getVolume()} m3")