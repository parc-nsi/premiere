# Génération de fichiers aux formats `pdf`, `markdown`, `html`, `slide-html` à partir d'un seul fichier source `***-source.md` 

* Sources documentaires : 
  * Markdown et Pandoc : <https://enacit.epfl.ch/cours/markdown-pandoc/>
  * Pandoc Guide : [https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html)
  * Filtres Pandoc : 
    * [https://pandoc.org/filters.html](https://pandoc.org/filters.html)
    * Filtres en Python : [pandocfilters](https://github.com/jgm/pandocfilters)
  * Make : <https://ensiwiki.ensimag.fr/images/e/eb/Makefile.pdf>
  * Mkdocs : merci à Franck Chambon et tous les participants de ce post du forum NSI : <https://mooc-forums.inria.fr/moocnsi/t/mkdocs-une-solution-ideale/1758>
* Placer le fichier `Makefile` contenu dans ce répertoire dans le même répertoire que le fichier source  `***-source.md`
* `indentation_mkdocs.py` sert à décaler de 4 espace les blocs de divs pandoc délimités par :::div(nom personnalisé) et ::: 
Ce prétraitement est nécessaire avant d'appliquer le filtre pandoc pour un export de la source vers un markdown compatible avec Mkdocs.

~~~
FILE=$(wildcard *source.md)
TARGET=$(FILE:source.md=.pdf) $(FILE:source.md=.tex) $(FILE:source.md=tmp-mkdocs.md)  $(FILE:source.md=git.md)

all: $(TARGET)

%.pdf: %source.md
	pandoc -s $< --listings --template="../../../Pandoc/template-pandocV1.tex" --filter ../../../Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes+multiline_tables --toc -V toc-title:"Table des matières" -o $@
	
%.tex: %source.md
	pandoc -s $< --listings --template="../../../Pandoc/template-pandocV1.tex" --filter ../../../Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes+multiline_tables --toc -V toc-title:"Table des matières" -o $@

%tmp-mkdocs.md: %source.md
	python3 ../../../Pandoc/indentation_mkdocs.py $<

%git.md: %tmp-mkdocs.md
	pandoc -s   --filter ../../../Pandoc/filtre.py --webtex  -V colorlinks --toc  -V toc-title:"Table des matières" -f markdown+table_captions+link_attributes+multiline_tables -t gfm  $<  -o $@
~~~

* Modifier éventuellement les chemins relatifs, pour que dans chaque répertoire où s'effectue la compilation, le `Makefile` puisse retrouver les templates qu ise trouvent dans le répertoire `Pandoc` :
 
~~~
