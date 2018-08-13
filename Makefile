targets = thesis.pdf
tmpdir = .tmp

all: $(targets)

view:
	evince .tmp/$(targets)

pdflatex = pdflatex -shell-escape -interaction=errorstopmode -halt-on-error -output-dir=$(tmpdir)

%.pdf: %.tex library.bib
	# rm -rf .tmp
	mkdir -p $(tmpdir)
	$(pdflatex) $<
	BSTINPUT="$(tmpdir):" TEXMFOUTPUT="$(tmpdir):" bibtex $(tmpdir)/$*
	$(pdflatex) $<
	$(pdflatex) $<

clean:
	rm -rf $(targets) $(tmpdir)