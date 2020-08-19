#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, stat, subprocess
from datetime import date

author = "Simon Fredrich"
# get meta details for generating folder and .tex file
change_author = input("Willst du den Autor '"+author+"' ändern? (J/n) ")
# check if author should be changed
if (change_author in ("J","j","Y","y")):
    author = input("Autor: ")
topic = input("Thema: ")
# make topic fit folder structure
topic = topic.replace(" ", "_")

# compose directory name
directory = topic

# format topic back to space form
topic = topic.replace("_", " ")

# get current date and format it the german way :D
day = str(date.today().day)
month = str(date.today().month)
year = str(date.today().year)
dot = "."
date_ = day + dot + month + dot + year

# get path to put new directory inside
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)

# list of .tex file content
latex_template_list = [
"\\documentclass[12pt, a4paper]{article}",
"% change size of headings",
"%--------------------------------------",
"\\usepackage[small]{titlesec}",
"%--------------------------------------",
"\\addtolength{\\hoffset}{-1.25cm}",
"\\addtolength{\\textwidth}{3.5cm}",
"\\addtolength{\\voffset}{-3.5cm}", 
"\\addtolength{\\textheight}{5cm}",
"\\setlength{\parskip}{0pt}",
"\\setlength{\parindent}{15pt}", 
"%encoding",
"%--------------------------------------",
"\\usepackage[utf8]{inputenc}", 
"\\usepackage[T1]{fontenc}", 
"%--------------------------------------",
"%German-specific commands",
"%--------------------------------------",
"\\usepackage[ngerman]{babel}", 
"%--------------------------------------",
"%Hyphenation rules",
"%--------------------------------------",
"\\usepackage{hyphenat}",
"\\hyphenation{Mathe-matik wieder-gewinnen}",
"%--------------------------------------", 
"%include some more packages",
"%--------------------------------------", 
"\\usepackage{amsthm}",
"\\usepackage{amsmath}", 
"\\usepackage{amssymb}",
"\\usepackage{amsfonts}",
"\\usepackage{amscd}",
"\\usepackage[colorlinks = true, linkcolor = black, citecolor = black, final]{hyperref}",
"\\pagestyle{empty}",
"%--------------------------------------",
"\\begin{document}",
"\\thispagestyle{empty}",
"{\\scshape "+author+"} \\hfill {\\scshape \\large "+topic+"} \\hfill {\\scshape "+date_+"}",
"\\smallskip", 
"\\hrule",
"\\bigskip", 
"% real content",
"\n\n",
"\\end{document}"
]

# list of .sh file content
bash_template_list = [
"!/bin/bash",
"latexmk -pdf main.tex",
"rm *.aux *.bbl *.toc *.blg *.fdb_latexmk *.fls *.log *.dvi *.lof *.out"
]

# create directory in current directory
def createDirectory(path):
    os.mkdir(path)

# create files with template list inside
def createFile(path, file_name, template_list):
    file_ = open(path + "/" + file_name, "w")
    for line in template_list:
        file_.write(line)
        file_.write("\n")
    file_.close()
    if (file_name == "build.sh"):
        build_file = path + "/" + file_name
        subprocess.check_call(['chmod', '+x', build_file]) 

if __name__ == "__main__":
    # running Process
    print("Generating...")
    createDirectory(path)
    createFile(path, "main.tex", latex_template_list)
    createFile(path, "build.sh", bash_template_list)
    print("Done!")
    print("Die Hausaufgabe zum Thema '" + topic + "' sollte\nam " + due_to + " fertig sein.")
    
