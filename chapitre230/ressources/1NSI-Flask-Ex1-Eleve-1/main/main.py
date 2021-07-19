#imports de modules 
from flask import Flask, render_template, request

#création d'une instance de l'application
app = Flask(__name__)

#dispatcheur de route / URL
@app.route('/')
def accueil():
    "Controleur de la route '/' "
    #retourne la vue associée : la page accueil.html
    return render_template('accueil.html')

#dispatcheur de route / URL
@app.route('/formulaire-connexion')
def formulaire():
    "Controleur de la route '/formulaire-connexion' "
    #retourne la vue associée : la page formulaire-connexion.html
    return render_template('formulaire-connexion.html')

#dispatcheur de route / URL
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
  "Controleur de la route '/connexion' "
  #si la méthode est POST
  if request.method == 'POST':
    #les valeurs des paramètres sont dans le dictionnaire request.form 
    ident = request.form['ident']
    password = request.form['pass']    
  else: #sinon c'est GET
    #la chaine de  paramètres est dans le dictionnaire request.args
    ident = request.args.get('ident', '') 
    password = request.args.get('pass', '')
  succes = password == 'secret'
  #retourne la vue associée en lui transmettant des paramètres
  return render_template('connexion.html', ident = ident, succes = succes)

#si le programme n'est pas importé dans un autre script Python
if __name__ == "__main__":
  # on ouvre un serveur en local sur le port 8000
  app.run(debug = True, host='0.0.0.0', port=8000)

   