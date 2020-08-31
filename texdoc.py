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
section = input("Abschnitt des Unterrichtsstoffes: ")
topic = input("Thema: ")


semester = "3"
# make topic fit folder structure
topic = topic.replace(" ", "_")

# get current date and format it the german way :D
day = str(date.today().day)
#normalize data
if (len(day) < 2):
    day = "0" + day
month = str(date.today().month)
# normalize data
if (len(month) < 2):
    month = "0" + month
year = str(date.today().year)
dot = "."
date_ = day + dot + month + dot + year

note_date = date_
change_note_date = input("Notizdatum ändern? (J/n) ")
change_date = False
# check if author should be changed
if (change_note_date in ("J","j","Y","y")):
    change_date = True
    note_date = input("Notizdatum: ")
    # check due_to date and correct if necessary with additional zeros
    note_date_split_list = note_date.split(".")
    note_date = ""
    for i in range(0, len(note_date_split_list)-1):
        if (len(note_date_split_list[i]) < 2): 
            note_date += "0" + note_date_split_list[i] + "." 
        else:
            note_date += note_date_split_list[i] + "." 
    note_date+=note_date_split_list[2]

# compose directory
dash = "-"
underscore = "_"
directory = date_.replace(".", dash) + underscore + topic
if (change_date):
    directory = note_date.replace(".", dash) + underscore + topic

# format topic back to space form
topic = topic.replace("_", " ")

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
"\\addtolength{\\hoffset}{-1cm}",
"\\addtolength{\\textwidth}{3.5cm}",
"\\addtolength{\\voffset}{-2.5cm}", 
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
"{\\scshape "+author+"} \\hfill {\\scshape \\large "+topic+"} \\hfill {\\scshape "+note_date+"}",
"\\smallskip", 
"\\hrule",
"\\bigskip", 
"% real content",
"\n\n",
"\\end{document}"
]

# new version of latex template list
latex_main = [
"\\input{packages.tex}",
"\\begin{document}",
"\\input{formalities.tex}",
"\\end{document}"
]

latex_formalities = [
"%--------------------------------------",
"% formalities",
"%--------------------------------------",
"\\noindent",
"\\begin{tabular*}{\\textwidth}{l @{\\extracolsep{\\fill}} r @{\\extracolsep{6pt}} l}",
"\\textit{\\name} && \\textit{\\created}\\\\             % Insira o seu nome dentro dos {}'.",
"\\textit{\\class} &&\\textit{\\term}\\\\",
"\\end{tabular*}\\",
"% big line to separate formalities",
"\\rule[1ex]{\\textwidth}{0.5pt}",
"% topic heading",
"%\\begin{center}{\\scshape \\Large \\topic}\\end{center}",
"\\begin{center}{\\Large \\topic}\\end{center}",
"%--------------------------------------",
"% set pagenumbering",
"%--------------------------------------",
"%\\setcounter{page}{1}",
"\\pagenumbering{arabic}",
"\\rfoot[]{\\thepage}",
"% INHALT %",
"\\bigskip"
]

latex_packages = [
"\\documentclass[12pt, a4paper]{article}",
"\\usepackage{amsthm}",
"\\usepackage{libertine}",
"\\usepackage[utf8]{inputenc}",
"\\usepackage[margin=1in]{geometry}",
"\\usepackage{amsmath,amssymb}",
"\\usepackage{multicol}",
"\\usepackage[shortlabels]{enumitem}",
"%--------------------------------------",
"% wichtige Informationen",
"%--------------------------------------",
"\\newcommand{\\class}{"+section+"}",
"\\newcommand{\\term}{"+semester+". Semester}",
"\\newcommand{\\topic}{"+topic+"}",
"\\newcommand{\\created}{"+note_date+"}",
"\\newcommand{\\timelimit}{}",
"\\newcommand{\\name}{"+author+"}",
"%--------------------------------------",
"% richtiges Encoding",
"%--------------------------------------",
"\\usepackage[utf8]{inputenc}",
"\\usepackage[T1]{fontenc}",
"%--------------------------------------",
"% German-specific commands",
"%--------------------------------------",
"\\usepackage[ngerman]{babel}",
"%--------------------------------------",
"% Hyphenation rules",
"%--------------------------------------",
"\\usepackage{hyphenat}",
"\\hyphenation{Mathe-matik wieder-gewinnen}",
"%--------------------------------------",
"% change size of headings",
"%--------------------------------------",
"\\usepackage[small]{titlesec}",
"%--------------------------------------",
"% change text-offset settings",
"%--------------------------------------",
"\\addtolength{\\voffset}{-1cm}",
"%\\addtolength{\\hoffset}{-1.25cm}",
"%\\addtolength{\\textwidth}{1.5cm}",
"\\usepackage{fancyhdr}"
]

# list of .sh file content
bash_template_list = [
"#!/bin/bash",
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
    createFile(path, "formalities.tex", latex_formalities)
    createFile(path, "packages.tex", latex_packages)
    createFile(path, "main.tex", latex_main)
    createFile(path, "build.sh", bash_template_list)
    print("Done!")
    print("Die Hausaufgabe zum Thema '" + topic + "' wurde erstellt!")
    
