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
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords # Import stopwords from nltk.corpus
from nltk.stem import WordNetLemmatizer
import en_core_web_sm
from nltk.corpus import wordnet as wn
import pandas as pd
from rake_nltk import Rake
import pytextrank



file = open("log.txt", "a+")
logger = Logger()

def preprocessing(text):
    logger.log(file, f"starting preprocessing")
    # Make lower
    text = text.lower()

    # Remove line breaks
    text = re.sub(r'\n', ' ', text)
    # Remove line breaks
    text = re.sub(r'\t', '', text)

    text = re.sub("[^A-Za-z0-9\s\.\,]+"," ", text)

    text = re.sub(r'[0-9]', ' ', text)

    text = text.split()

    with open(os.path.join("stopwords.txt"),'r') as useless_words:
        lis = useless_words.read().split("\n")
        try:
            stop_words = stopwords.words('english')
            logger.log(file, f"trying to load eng stopwords from model")

        except:
            logger.log(file, f"load failed downloading stopwords from nlkt")
            nltk.download('stopwords')
            stop_words = stopwords.words('english')
            lis = set(lis + stop_words)
        finally:
            lis = lis + ['hi', 'im']

            try:
                logger.log(file, f"trying loading wordlemma")
                lem = WordNetLemmatizer()
                lem.lemmatize("testing")
            except:
                logger.log(file, f"loading failed trying to download wordnetm and omw 1.4")
                #call the nltk downloader
                nltk.download('wordnet')
                nltk.download('omw-1.4')
                lem = WordNetLemmatizer() #stemming
            finally:
                logger.log(file, f"lemmatize words preprocessing done")
                text_filtered = [lem.lemmatize(word) for word in text if not word in lis]
                return " ".join(text_filtered)

def text_process(text):
    text = preprocessing(text)
    data = textrank(text)
    logger.log(file, f"text rank done")
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


def tfidf(text: str) -> list:
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text])

    feature_names = vectorizer.get_feature_names_out()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    
    df = df.transpose().reset_index()
    df.columns = ['words', 'value']
    df = df.sort_values('value', ascending = False)

    logger.log(file, f"tfidf done returning top 50 words")
    return df.loc[:50, 'words'].tolist()


def rake(text: str) -> list:
    r = Rake()

    r.extract_keywords_from_text(text)

    keywordList = []
    rankedList = r.get_ranked_phrases_with_scores()
    for keyword in rankedList:
        keyword_updated = keyword[1].split()
        keyword_updated_string    = " ".join(keyword_updated[:2])
        keywordList.append(keyword_updated_string)
        if(len(keywordList)>9):
            break
    logger.log(file, f"used rake now returning")
    return keywordList


def textrank(text):
    logger.log(file, f"spacy + text rank function starting")
    nlp = en_core_web_sm.load()
    nlp.add_pipe("textrank")
    doc = nlp(text)
    # examine the top-ranked phrases in the document
    return [text.text for text in doc._.phrases[:40] if len(text.text) < 30]
        
