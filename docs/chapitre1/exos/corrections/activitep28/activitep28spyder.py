
#%% Tracer un carré
from turtle import *

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

exitonclick()



#%% Utiliser une variable
from turtle import *

#initialisation de la variable cote
cote = 50
forward(cote)
right(90)
forward(cote)
right(90)
forward(cote)
right(90)
forward(cote)

exitonclick()


#%% Utiliser une boucle

from turtle import *

#initialisation de la variable cote
cote = 50
for i in range(4): #exécuter le corps de la boucle 4 fois
    forward(cote)  #première instruction du corps de la boucle
    right(90)      #deuxième instruction du corps de la boucle
print("Fini !")
exitonclick()

#%%Dessiner un polygone quelconque avec une boucle
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


#%%   Dessiner un polygone quelconque avec une fonction
from turtle import *

def polygone(n, cote):
    """Tracer un polygone a n cotes de longueur cote"""
    #initialisation de la variable angle
    angle = 360 / n
    #boucle 
    for i in range(n): #exécuter le corps de la boucle 4 fois
        forward(cote)  #première instruction du corps de la boucle
        right(angle)      #deuxième instruction du corps de la boucle
    
#appel de fonction
polygone(6, 100)
exitonclick()


exitonclick()

#%% Dessiner une rosace
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



