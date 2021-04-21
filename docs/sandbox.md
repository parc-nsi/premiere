---
title: My special title
bottles:
  whine: 500
  beer: 123
---


<https://mkdocs-macros-plugin.readthedocs.io>


# Variables définies dans l'en-tête yaml :

{{ page.meta.bottles.whine }}.


# Langage de template Jinja2 

## Boucles :

### List of users
{% set users = ['joe', 'jill', 'david', 'sam'] %}
{% for user in users %}
1. {{ user }}
{% endfor %}

# Application d'un filtre 

{{ context(navigation.pages) | pretty }}


# Blocs personnalisés avec super_fences

* Références : 
  * <https://github.com/facelessuser/pymdown-extensions/issues/928>
  * <https://facelessuser.github.io/pymdown-extensions/>





