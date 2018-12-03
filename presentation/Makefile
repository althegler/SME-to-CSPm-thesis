targets = slides.pdf
tmpdir = .tmp

all: $(targets)

view:
	open .tmp/$(targets)

pdflatex = pdflatex -shell-escape -interaction=errorstopmode -halt-on-error -output-dir=$(tmpdir)

%.pdf: %.tex
	mkdir -p $(tmpdir)
	$(pdflatex) $<

clean:
	rm -rf $(targets) $(tmpdir)
