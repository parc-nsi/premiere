#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pandoc filter to convert divs with latex="true" to LaTeX
environments in LaTeX output. The first class
will be regarded as the name of the latex environment
e.g.
<div latex="true" class="note abc">...</div>
will becomes
\begin{note}...\end{note}
"""

from pandocfilters import toJSONFilter, RawBlock, Div, stringify, Strong, Para, walk
import json
import sys

def latex(x):
    return RawBlock('latex', x)

def convertdivs(key, value, format, meta):
    global compteur_histoire, compteur_activite, compteur_remarque, compteur_exercice, compteur_theoreme, compteur_definition, compteur_propriete, compteur_cours, compteur_exemple,compteur_methode
    if key == 'Div':
        [[ident, classes, kvs], contents] = value
        #if ["latex","true"] in kvs:
        #print(kvs)
        if format == "latex":            
            if ident == "":
                label = ""
            else:
                label = '\\label{' + ident + '}'
            options =   ','.join('='.join(couple) for couple in kvs)
            #deboggage
            #f.write(str(contents[0]['c']))
            if classes[0] == 'minipage':
                for clef, val in kvs:
                    if clef == "width":
                        options = val
                        break                
                decoupage = []
                token = {'t': 'Str', 'c': '&'}
                for k in range(len(contents[0]['c'])):
                    if (contents[0]['c'][k] == token and k > 0) or (k < len(contents[0]) and contents[0]['c'][k] == token and contents[0]['c'][k-1] != token):
                        decoupage.append(k)
                i = 0
                body = [latex('\\begin{tabular}{' + 'c' * (len(decoupage) + 1) + '}')] 
                for d in decoupage:
                    body = body + [latex('\\begin{' + classes[0] + '}{' + options + '}')] +[{'t': 'Para', 'c': contents[0]['c'][i:d] }]+  [latex('\\end{' + classes[0] + '} &')]
                    i = d + 1
                body = body + [latex('\\begin{' + classes[0] + '}{' + options + '}' + label)] +[{'t': 'Para', 'c': contents[0]['c'][i:] }]+  [latex('\\end{' + classes[0] + '} \end{tabular}')]
              
            else:
                body = [latex('\\begin{' + classes[0] + '}{' + options + '}' + label)] + contents + [latex('\\end{' + classes[0] + '}')]
            if ["center","true"] in kvs:
                 left = [latex('\\begin{center}')]
                 right =  [latex('\\end{center}')]
            else:
                left = []
                right = []
            return left + body + right
        elif format == "gfm":  #pour GitHub markdown
            if classes[0] == "exercice":                
                compteur_exercice += 1
                return  [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! tip "Exercice ' + str(compteur_exercice) + str('"')}]}]  +  contents
            elif classes[0] == "theoreme":
                #f.write(str(contents[0]['c']))
                compteur_theoreme += 1
                return [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! note "Théorème ' + str(compteur_theoreme) + str('"')}]}]    + contents
            elif classes[0] == "definition":
                compteur_definition += 1
                return  [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! note "Définition ' + str(compteur_definition) + str('"')}]}]      + contents
            elif classes[0] == "propriete":
                compteur_propriete += 1
                return  [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! note "Propriété ' + str(compteur_propriete) + str('"')}]}]      + contents
            elif classes[0] == "cours":
                compteur_cours += 1
                return  [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! note "Point de cours ' + str(compteur_cours) + str('"')}]}]       + contents
            elif classes[0] == "exemple":
                compteur_exemple += 1
                return  [{'t': 'Plain', 'c':[{'t': 'Str', 'c' : '!!! example "Exemple ' + str(compteur_exemple) + str('"')}]}]       + contents
            elif classes[0] == "activite":
                compteur_activite += 1
                return  [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! info "Activité ' + str(compteur_activite) + str('"')}]}]     + contents
            elif classes[0] == "histoire":
                compteur_histoire += 1
                return  [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! abstract "Histoire ' + str(compteur_histoire) + str('"')}]}]       + contents
            elif classes[0] == "methode":
                compteur_methode += 1
                return  [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! success "Méthode ' + str(compteur_methode) + str('"')}]}]       + contents
            elif classes[0] == "rque":
                return  [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! warning "À retenir ' + str('"')}]}]      + contents         
                compteur_remarque += 1
            elif classes[0] in ["synthese","memo"]:
                return  [{'t': 'Plain', 'c': [{'t': 'Str', 'c' : '!!! abstract "Synthèse ' + str('"')}]}]     + contents               
            elif "minipage" or "center" in classes:
                return   contents


compteur_remarque = 0                
compteur_exercice = 0
compteur_theoreme = 0
compteur_definition = 0
compteur_propriete = 0
compteur_exemple = 0
compteur_cours = 0
compteur_methode = 0
compteur_activite = 0
compteur_histoire = 0
#f = open('sortie3.txt', 'w') #deboggage

if __name__ == "__main__":
    toJSONFilter(convertdivs)
   

