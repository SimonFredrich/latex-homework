#!/bin/bash
latexmk -pdf main.tex
rm *.aux *.bbl *.toc *.blg *.fdb_latexmk *.fls *.log *.dvi *.lof *.out
