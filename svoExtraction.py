import nltk
import spacy
import textacy
from keras.layers import Embedding, Bidirectional, Dense, Dropout, BatchNormalization
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
from nltk import word_tokenize, re
from rasa import model
import pandas as pd
from spacy import lemmatizer

nlp = spacy.load('en_core_web_sm')

text=input("Enter the text to find the triplet: ")
str=nlp(text)

def load_dataset(filename):
    df = pd.read_csv(filename, encoding="latin1",
                     names=["Sentence", "Intent"])
    intent = df["Intent"]
    unique_intent = list(set(intent))
    sentences = list(df["Sentence"])

    return (intent, unique_intent, sentences)


def cleaning(sentences):
    words = []
    for s in sentences:
        clean = re.sub(r'[^ a-z A-Z 0-9]', " ", s)
        w = nltk.word_tokenize(clean)
        # lemmatizing
        words.append([lemmatizer.lemmatize(i.lower()) for i in w])


    return words

def create_tokenizer(words,
                  filters = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'):
  token = Tokenizer(filters = filters)
  token.fit_on_texts(words)
  return token
def max_length(words):
  return(len(max(words, key = len)))
def encoding_doc(token, words):
  return(token.texts_to_sequences(words))

def findTriplets(str):
    tuple_data=textacy.extract.subject_verb_object_triples(str)
    return tuple_data

def creatingLists(tuple_data):
    tuple_to_lists=list(tuple_data)
    return tuple_to_lists


def displaySubjectVerbObject(tuples_to_lists):
    for item in tuples_to_lists:
        print(item)


tuple_data=findTriplets(str)
list=creatingLists(tuple_data)
displaySubjectVerbObject(list)