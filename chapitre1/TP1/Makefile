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

