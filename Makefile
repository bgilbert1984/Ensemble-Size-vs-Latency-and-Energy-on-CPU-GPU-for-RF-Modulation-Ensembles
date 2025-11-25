# Makefile for Ensemble Size vs Latency/Energy Paper
# 
# Usage:
#   make pdf       - Generate the full paper PDF
#   make figs      - Generate all figures 
#   make clean     - Clean auxiliary LaTeX files
#   make fresh     - Clean everything and rebuild

# Main document
MAIN = main_ensemble_latency_energy
PDF = $(MAIN).pdf
TEX = $(MAIN).tex

# Figure dependencies
FIGS = figs/latency_vs_ensemble_size.pdf figs/energy_vs_ensemble_size.pdf

# Data dependencies  
DATA = data/ensemble_callouts.tex data/ensemble_table.tex

.PHONY: all pdf figs clean fresh

# Default target
all: pdf

# Generate the PDF
pdf: $(PDF)

$(PDF): $(TEX) $(FIGS) $(DATA)
	pdflatex -interaction=nonstopmode $(MAIN).tex
	pdflatex -interaction=nonstopmode $(MAIN).tex
	@echo "✅ Generated $(PDF)"
	@ls -lh $(PDF)

# Generate figures
figs: $(FIGS)

$(FIGS): scripts/gen_placeholder_figs.py
	python3 scripts/gen_placeholder_figs.py

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.bbl *.blg *.out *.toc *.fdb_latexmk *.fls *.synctex.gz

# Clean everything and rebuild
fresh: clean
	rm -f $(PDF)
	$(MAKE) pdf

# Show paper info
info:
	@echo "Paper: Ensemble Size vs Latency and Energy"
	@echo "Main file: $(TEX)"
	@echo "Output: $(PDF)"
	@echo "Figures: $(FIGS)"
	@echo "Data files: $(DATA)"