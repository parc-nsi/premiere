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


~~~mermaid

%%{init: {'theme': 'dark' } }%%
graph TD
A --> B

~~~

```mermaid
graph TD
    A[Hard] -->|Text| B(Round)
    B --> C{Decision}
    C -->|One| D[Result 1]
    C -->|Two| E[Result 2]
```

???- note "Collapsed"
    ```mermaid
    graph TD
    A[Client] --> B[Load Balancer]
    ```
    This is additional text.





```graphviz engine="dot"
digraph G {
  node [shape=box]

  actor [shape=doubleoctagon];

  subgraph cluster {
    node [style=filled shape=cylinder];
    redis; postgres; rabbitmq; elasticsearch;
    label="Databases";
  }
  
  actor -> webserver [dir=both color="red:blue"];
  webserver -> rabbitmq;
  rabbitmq -> worker [weight=3 label="task broker"];
  webserver -> redis [dir=both color="red:blue"];
  worker -> redis [dir=both color="red:blue" label="task caching\nlike proxy sessions"];
  webserver -> { elasticsearch postgres } [dir=both color="red:blue"];
  worker -> { postgres elasticsearch };
}
```