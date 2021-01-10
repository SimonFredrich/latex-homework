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


semester = "4"
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

# new version of latex template list
latex_main = [
"\\input{preamble}",
"\\begin{document}",
"\\input{information}",
"",
"",
"",
"",
"",
"",
"\\end{document}"
]

latex_information = [
"%--------------------------------------",
"% information and header",
"%--------------------------------------",
"\\noindent",
"\\begin{tabular*}{\\textwidth}{l @{\\extracolsep{\\fill}} r @{\\extracolsep{6pt}} l}",
"\\textit{\\name} && \\textit{\\created}\\\\",
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
"\\bigskip",
"% INHALT %"
]

latex_preamble = [
"\\documentclass[12pt, a4paper]{article}",
"\\usepackage{amsthm}",
"\\usepackage{libertine}",
"\\usepackage[utf8]{inputenc}",
"\\usepackage[margin=1in]{geometry}",
"\\usepackage{amsmath,amssymb}",
"\\usepackage{multicol}",
"\\usepackage[shortlabels]{enumitem}",
"\\usepackage{siunitx}",
"\\sisetup{",
"    mode = math,",
"    detect-all,",
"    exponent-product = \\cdot,",
"    number-unit-separator=\\text{\,},",
"    output-decimal-marker={\\text{,}},",
"}",
"\\usepackage{float}",
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
"% wichtige Informationen",
"%--------------------------------------",
"\\newcommand{\\class}{"+section+"}",
"\\newcommand{\\term}{"+semester+". Semester}",
"\\newcommand{\\topic}{"+topic+"}",
"\\newcommand{\\created}{"+note_date+"}",
"\\newcommand{\\timelimit}{}",
"\\newcommand{\\name}{"+author+"}",
"%--------------------------------------",
"% change text-offset settings",
"%--------------------------------------",
"\\addtolength{\\voffset}{-1cm}",
"%\\addtolength{\\hoffset}{-1.25cm}",
"%\\addtolength{\\textwidth}{1.5cm}",
"\\usepackage{fancyhdr}"
"%--------------------------------------",
"% include inkscape figures",
"%--------------------------------------",
"\\usepackage{import}",
"\\usepackage{pdfpages}",
"\\usepackage{transparent}",
"\\usepackage{xcolor}",
"\\newcommand{\\incfig}[2][1]{%",
"    \\def\\svgwidth{#1\\columnwidth}",
"    \\import{./figures/}{#2.pdf_tex}",
"}",
"\\pdfsuppresswarningpagegroup=1",
"%--------------------------------------"
"% quote solution",
"%--------------------------------------",
"\\let\\oldquote'",
"\\newif\\ifquoteopen",
"\\catcode`\\'=\\active",
"\\makeatletter",
"% we have to redefine \\pr@m@s to use an active '",
"\\def\\pr@m@s{%",
"  \\ifx'\\@let@token",
"    \\expandafter\\pr@@@s",
"  \\else",
"    \\ifx^\\@let@token",
"      \\expandafter\\expandafter\\expandafter\\pr@@@t",
"    \\else",
"      \\egroup",
"    \\fi",
"  \\fi}",
"\\protected\\def'{%",
"  \\ifmmode",
"    \\expandafter\\active@math@prime",
"  \\else",
"    \\expandafter\\active@text@prime",
"  \\fi}",
"\\def\\active@text@prime{%",
"   \\@ifnextchar'{%",
"     \\ifquoteopen",
"       \\global\\quoteopenfalse\\grqq\\expandafter\\@gobble",
"     \\else",
"       \\global\\quoteopentrue\\glqq\\expandafter\\@gobble",
"     \\fi",
"   }{\\oldquote}%",
"}",
"\\makeatother"
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
    createDirectory(path + "/figures")
    print("dir 'figures' created")
    createFile(path, "information.tex", latex_information)
    createFile(path, "preamble.tex", latex_preamble)
    createFile(path, "main.tex", latex_main)
    print("information.tex, preamble.tex and main.tex created")
    createFile(path, "build.sh", bash_template_list)
    print("build.sh created")
    print("...'" + topic + "' Done!")
    
