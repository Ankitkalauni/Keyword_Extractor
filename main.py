from nbformat import read
import streamlit as st
from io import StringIO 
import docx2txt
from logger import Logger
from PyPDF2 import PdfFileReader
import os
import time
from streamlit_quill import st_quill
from process import text_process, text_to_pdf, show_pdf, create_download_link, text_doc
from docx import Document




file = open("log.txt", "a+")
logger = Logger()

def save_to_file(str_data, readmode = "w"):
    with open("./userdata.txt", readmode) as file_obj:
        file_obj.write(str_data)
    logger.log(file, "file saved")

def process_data(uploaded_file):
        data = docx2txt.process(uploaded_file)
        logger.log(file, "data processed to str")
        return data

def get_doc(uploaded_file):
    if uploaded_file is not None:

        if st.button("proceed"):

            st.subheader('Edit Data')
            str_data = process_data(uploaded_file)
        
            st.session_state['str_value'] = str_data
            


            logger.log(file, "updated data to session from doc string")
            return str_data

def run_editor(str_data, key = "editor"):
    # Spawn a new Quill editor
    logger.log(file, "starting editor")
    content = st_quill(value = str_data,key=key)
        
    st.session_state['str_value'] = content
    logger.log(file, "returning editor new content")
    return content


if "load_state" not in st.session_state:
    st.session_state['load_state'] = False


if __name__ == '__main__':
    st.session_state['user_data'] = 0
    st.session_state['load_state'] = True
    boundary = "\n"*4 + "=====Keywords======" + "\n"*4

    logger.log(file, "init done")
    uploaded_file = st.file_uploader("Upload Doc or Docx File Only",type = [".doc","docx"])
    str_data = get_doc(uploaded_file)

    
    data = run_editor(str_data)
    if st.session_state['str_value'] is not None:
        st.session_state['user_data'] = 1

    if st.session_state['user_data']:
        if st.button("save & Extract") or st.session_state['load_state']:
            logger.log(file, "Saving userdata")
            data = data + boundary
            save_to_file(data)
            logger.log(file, "user edited data saved. no extracting data")
            save_to_file(text_process(data), readmode="a+")

            logger.log(file, "data extracted and appended to the original userdata")

            
            genre = st.radio(
            "Download as",
            ('PDF', 'DOC'))

            with open("userdata.txt", 'r', encoding="latin-1") as df:
                if genre == 'PDF':
                    text_to_pdf(df, 'keywords.pdf')
                    with open("./keywords.pdf", "rb") as pdf_file:
                        PDFbyte = pdf_file.read()

                        st.download_button(label="Export as PDF",
                        data=PDFbyte,
                        file_name="keywords.pdf",
                        mime='application/octet-stream')

                else:
                    text_doc(df, 'keywords')
                    with open("./keywords.doc", "rb") as doc_file:
                        docbyte = doc_file.read()

                        st.download_button(label="Export as DOC",
                        data=docbyte,
                        file_name="keywords.doc",
                        mime='application/octet-stream')





            

            
                



            

            
    