import streamlit as st
from io import StringIO 
import docx2txt
from logger import Logger
from PyPDF2 import PdfFileReader
import os
import time
from streamlit_quill import st_quill


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


def run_editor(str_data):
    # Spawn a new Quill editor
    logger.log(file, "starting editor")
    content = st_quill(value = str_data,key="editor")
        
    st.session_state['str_value'] = content
    logger.log(file, "returning editor new content")
    return content

if __name__ == '__main__':  
    st.session_state['user_data'] = 0
    uploaded_file = st.file_uploader("Upload Doc or Docx File Only",type = [".doc","docx"])
    str_data = get_doc(uploaded_file)

    
    data = run_editor(str_data)
    if st.session_state['str_value'] is not None:
        st.session_state['user_data'] = 1

    if st.session_state['user_data']:
        if st.button("save"):
            save_to_file(data)

            st.write(data)
    
    