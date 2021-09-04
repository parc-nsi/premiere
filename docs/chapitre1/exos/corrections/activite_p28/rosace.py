
from turtle import *

def polygone(n, cote):
    """Tracer un polygone a n cotes de longueur cote"""
    #initialisation de la variable angle
    angle = 360 / n
    #boucle 
    for i in range(n): #exécuter le corps de la boucle 4 fois
        forward(cote)  #première instruction du corps de la boucle
        right(angle)      #deuxième instruction du corps de la boucle

for i in range(40):
    #appel de fonction
    polygone(3, 100)
    right(9)
exitonclick()
