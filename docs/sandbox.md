
# Insertion de graphiques en langages dot 

Module de Rodrigo Schwencke, voir  <https://pypi.org/project/mkdocs-markdown-graphviz/> et <https://gitlab.com/rodrigo.schwencke/mkdocs-markdown-graphviz>.


```graphviz dot attack_plan.svg
digraph G {
    rankdir=LR
    Earth [peripheries=2]
    Mars
    Earth -> Mars
}
```


```graphviz dot attack_plan.png
digraph G {
    rankdir=LR
    Earth [peripheries=2]
    Mars
    Earth -> Mars
}
```
