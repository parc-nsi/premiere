
from turtle import *

#initialisation de la variable cote
cote = 50
#initialisation de la variable n
n = 12
#initialisation de la variable angle
angle = 360 / n
#boucle 
for i in range(n): #exécuter le corps de la boucle 4 fois
    forward(cote)  #première instruction du corps de la boucle
    right(angle)      #deuxième instruction du corps de la boucle
print("Fini !")

exitonclick()