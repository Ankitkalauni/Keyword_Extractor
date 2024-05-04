
<center> <h1>Keyword Extractor </h1> </center>

The keyword extraction technique will sift through the whole set of data in minutes and obtain the words and phrases that best describe each subject. This way, you can easily identify which parts of the available data cover the subjects you are looking for while saving your teams many hours of manual processing.


**Streamlit app:** https://keywordextract.streamlit.app/

# How to download
0. Python version 3.9.6
1. Clone this repo to your local machine
2. make virtualenv (recommended)
3. open and change terminal location to the project directory
4. run the below command after activating the virtualenv

        pip install -r requirement.txt

5. now run the below command

        streamlit run main.py


The following text will be shown


    $ streamlit run main.py

    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.0.105:8501



**Open a browser with the local URL given in a terminal**

## Home page

* Below is the home page of the keyword Extractor Streamlit app
___
![Home Page](https://raw.githubusercontent.com/Ankitkalauni/Keyword_Extractor/main/images/home_page.png)


## Upload a doc file

* you can upload doc/docx file (max 200mb)
___
![Upload doc](https://raw.githubusercontent.com/Ankitkalauni/Keyword_Extractor/main/images/upload.png)


## Process and edit the document online

* process the file and edit it online
___
![edit doc](https://raw.githubusercontent.com/Ankitkalauni/Keyword_Extractor/main/images/edit.png)



## Extract the keywords and download them as a PDF/DOC file

* Apply keyword extraction to the edited doc file and download it as a PDF/DOC file.
* For now, only spacy with textrank,Rake and tf-idf are implemented.

**Currently using Spacy with textrank layer**
___
![download file](https://raw.githubusercontent.com/Ankitkalauni/Keyword_Extractor/main/images/download.png)


## Save document with Keywords at the end of the download document

* The kewords will be appended to the last of the downloaded document.

___
![keywords](https://raw.githubusercontent.com/Ankitkalauni/Keyword_Extractor/main/images/keywords.png)

# Preprocessing

Data preprocessing is an essential step in building a Machine Learning model and depending on how well the data has been preprocessed; the results are seen.

In NLP, text preprocessing is the first step in the process of building a model.

The various text preprocessing steps are:

Tokenization
Lower casing
Stop words removal
Stemming
Lemmatization
These various text preprocessing steps are widely used for dimensionality reduction.

Learn more about - [Text Preprocessing in Natural Language Processing](https://towardsdatascience.com/text-preprocessing-in-natural-language-processing-using-python-6113ff5decd8)


## Contribution

* If you have better idea and want to update this tool. please contribute to this project.


<center> <h3><a href = "https://keywordextract.streamlit.app/">Try this tool Online</a>
