from cmath import log
import spacy
import re
import string
import textwrap
from fpdf import FPDF
from logger import Logger
import os
import base64
import streamlit as st
from docx import Document

import en_core_web_sm
nlp = en_core_web_sm.load()

file = open("log.txt", "a+")
logger = Logger()

def preprocessing(text):
    logger.log(file, "started cleaning data")
    # Make lower
    text = text.lower()

    # Remove line breaks
    text = re.sub(r'\n', ' ', text)
    # Remove line breaks
    text = re.sub(r'\t', '', text)

    text = re.sub("[^A-Za-z0-9\s]+"," ", text)

    text = re.sub(r'[0-9]', ' ', text)

    text = text.split()

    with open(os.path.join("stopwords.txt"),'r') as useless_words:
        lis = useless_words.read().split("\n")

        lis = lis + ['hi', 'im']    

        text_filtered = [word for word in text if not word in lis]

    
    return " ".join(set(text_filtered))

def text_process(text):
    text = preprocessing(text)
    doc = nlp(text)

    data = doc.ents #Named Entity i will use more methods later like tf-idf..
    data = ", \n".join(str(d) for d in data)

    if data == "":
        data = "None Keyword Found"
    logger.log(file, "data cleaned and returned")
    return data


def text_to_pdf(text, filename):
    pdf = FPDF()  
    pdf.add_page()

    pdf.set_font("Arial", size = 15)
    
    # insert the texts in pdf
    pdf.set_line_width(1)
    for x in text:
        pdf.cell(0,5, txt = x, ln = 1, align = 'L')
    
    # save the pdf with name .pdf
    pdf.output(filename) 

    logger.log(file, "PDF File saved")

def text_doc(file, filename):
    doc = Document()
    line = file.read()
    doc.add_paragraph(line)
    doc.save(filename + ".doc")


