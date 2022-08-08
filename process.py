import spacy
import re
import string
import nltk
# python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")


def preprocessing(text):
    # Make lower
    text = text.lower()

    # Remove line breaks
    text = re.sub(r'\n', '', text)
    # Remove line breaks
    text = re.sub(r'\t', '', text)

    text = re.sub("[^A-Za-z0-9\s]+"," ", text)

    text = re.sub(r'[0-9]', ' ', text)

    text = text.split()

    with open("./stopwords.txt",'r') as useless_words:
        lis = useless_words.read().split("\n")

        lis = lis + ['hi', 'im']    

        text_filtered = [word for word in text if not word in lis]


    return " ".join(text_filtered)

def text_process(text):
    text = preprocessing(text)
    with open('temp.txt', 'w') as temp:
                temp.write(text)
    doc = nlp(text)

    data = doc.ents
    data = " ".join(str(d) for d in data)
    return data