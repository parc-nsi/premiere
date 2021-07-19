# -*- coding: utf-8 -*-
"""
Exemples du cours sur l'algorithme knn
"""

#%% Import des modules
import math
from utilitaires_knn import *
from knn import *


#%% Exemple 1 : Pokemons Feu et Roche / 2 descripteurs : vitesse et defense

#chargement de la table
table_pokemons = charger_fichier_entete('./datas/pokemons.csv')

#postcondition
assert table_pokemons[0] == {'nom': 'Rattata',
 'vie': '30',
 'attaque': '56',
 'defense': '35',
 'vitesse': '72',
 'type': 'Normal'}

#filtrage de la table
table_pokemons_feu_roche = [pok for pok in table_pokemons 
                   if pok['type'] in ['Roche', 'Feu']]

#Nouveau Pokemon
nouveau_pokemon = {'vitesse':58, 'attaque' : 120 , 'defense' : 65, 'vie' : 100 }

#Distance avec le pemier pokemon de la table
salameche = table_pokemons_feu_roche[0]
print("Distance entre nouveau_pokemeon et salameche  (vie et defense)", distance_euclidienne(nouveau_pokemon, salameche, ['vitesse', 'defense']))

#Tableau de distances
tab_distance = table_distance_nouveau(table_pokemons_feu_roche, nouveau_pokemon, distance_euclidienne, 'type',                                      ['vitesse', 'defense'])

k_voisins = trier_puis_extraire(tab_distance, 5)


#%% Calculs de distances
import matplotlib.pyplot as plt

#%% Représentation de la distance euclidienne dans le plan
pointA = [58, 60]
pointB = [80, 58]

plt.annotate('A', pointA)
plt.annotate('B', pointB)
plt.plot([pointA[0], pointB[0]], [pointA[1], pointB[1]], marker = 'o', color = 'red')
plt.title('Distance euclidienne')
plt.show()


#%% Représentation de la distance de Manhattan dans le plan
pointA = [58, 60]
pointB = [80, 58]

plt.annotate('A', pointA)
plt.annotate('B', pointB)
plt.plot([pointA[0], pointA[0], pointB[0]], [pointA[1], pointB[1], pointB[1]], marker = 'o', color = 'red')
plt.title('Distance de Manhattan')
plt.show()

#%% Influence du paramètre k

table_pokemons = charger_fichier_entete('./datas/pokemons.csv')
table_pokemons_feu_roche = [pok for pok in table_pokemons if pok['type'] in ['Feu', 'Roche']]
nouveau_pokemon = {'vitesse':58, 'attaque' : 120 , 'defense' : 65, 'vie' : 100 }
for k in range(1, 11):
    print(f"k = {k}, etiquette = {etiquetage_knn(table_pokemons_feu_roche, nouveau_pokemon, 'type', ['vitesse', 'defense'], k)}")

    




