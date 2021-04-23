---
title: My special title
bottles:
  whine: 500
  beer: 123
---

Référence pour les macros Mkdocs : <https://mkdocs-macros-plugin.readthedocs.io>


# Variables définies dans l'en-tête yaml :

Ici l'en-tête est :

~~~
title: My special title
bottles:
  whine: 500
  beer: 123
~~~

En écrivant `\{\{ page.meta.bottles.whine \}\}` (sans les \ ), on obtient :
{{ page.meta.bottles.whine }}. Voir <https://mkdocs-macros-plugin.readthedocs.io/en/latest/#variables>

# Abréviations

On peut insérer le contenu d'un fichier [d'abréviations](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/), en modifiant éventuellement le répertoire par défaut ([`docs_dir`](https://www.mkdocs.org/user-guide/configuration/#docs_dir), voir cette [doc](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#changing-the-directory-of-the-includes)) pour y placer les fichiers à inclure. 

On utilise la syntaxe Jinja2 `{% include 'abbreviations.md' %}`.

{% include 'abbreviations.md' %}

Si on a défini l'abréviation `[Python]:https://docs.python.org/3.7/library/cgi.html` , on peut obtenir alors un lien hypertexte en écrivant le raccourci `[Python][Python]`.

[Python][Python]

On peut ainsi centraliser des abréviations et les mettre à jour automatiquement sur l'ensemble d'un site.

# Langage de template Jinja2 

## Boucles :

~~~
{% set users = ['joe', 'jill', 'david', 'sam'] %}
{% for user in users %}
1. {{ user }}
{% endfor %}
~~~

donne 

{% set users = ['joe', 'jill', 'david', 'sam'] %}
{% for user in users %}
1. {{ user }}
{% endfor %}


# Insertion de scripts


En écrivant `\{\{ script('python', 'solution_scrabble.py') \}\}` (sans les \ )

(Macro de Franck Chambon dans `main.py`) donne :

{{ script('python', 'solution_scrabble.py') }}


!!! warning "Remarque" 

    * Pour insérer un script Python, la macro `script` définie dans `main.py` (Franck Chambon) prend en argument le chemin relatif  du script par rapport au fichier ma_page.md. Ci-dessous on donne un autre exemple avec , un fichier Python dans sous-répertoire `'automatismes/automatismes.py'`, on écrit alors   `\{\{ script('python', 'automatismes/automatismes.py') \}\}` (sans les \).

    * En revanche, avec la macro `basthon` définie dans `main.py` (Franck Chambon), l'insertion ne se fait pas dans le fichier markdown mais plus tard dans le fichier HTML généré et là le chemin relatif a changé (voir explication [ici](https://mkdocs-macros-plugin.readthedocs.io/en/latest/tips/#how-do-i-deal-with-relative-links-to-documentsimages)).

    * Si `mkdocs-jupyter` n'est pas activé, on écrira `\{\{ basthon('../solution_scrabble.py', 800) \}\}` et `\{\{ basthon('../automatismes/automatismes.py',800) \}\}`.
    
    * Si `mkdocs-jupyter` est  activé, lors de la compilation celui-ci a créé un répertoire par fichier `.py` ou `.ipynb` avec un `index.html` (export en HTML) et le fichier source (si option `include_source` à `true`), dans ce cas il faut rajouter un répertoire dans le chemin relati. Ici par exemple : `\{\{ basthon('../solution_scrabble/solution_scrabble.py', 800) \}\}` et `\{\{ basthon('../automatismes/automatismes/automatismes.py',800) \}\}`.

{{ script('python', 'automatismes/automatismes.py') }}


{{ basthon('../solution_scrabble/solution_scrabble.py', 800) }}


{{ basthon('../automatismes/automatismes/automatismes.py',800) }}

# Blocs personnalisés avec super_fences

Graphiques avec mermaid2 : `https://github.com/fralau/mkdocs-mermaid2-plugin` :

    ```mermaid
    graph TB
        c1-->a2
        subgraph one
        a1-->a2
        end
        subgraph two
        b1-->b2
        end
        subgraph three
        c1-->c2
        end
    ```

donne

```mermaid
graph TB
    c1-->a2
    subgraph one
    a1-->a2
    end
    subgraph two
    b1-->b2
    end
    subgraph three
    c1-->c2
    end
```

* Références : 
  * <https://github.com/facelessuser/pymdown-extensions/issues/928>
  * <https://facelessuser.github.io/pymdown-extensions/>





