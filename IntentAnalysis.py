from keras.layers import Embedding, Bidirectional, Dense, Dropout, BatchNormalization
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
from nltk import word_tokenize
from rasa import model
from sklearn import model_selection,preprocessing,linear_model,naive_bayes,metrics,svm
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn import decomposition,ensemble
import pandas,xgboost,numpy,textblob,string
from keras.preprocessing import text,sequence
from keras import layers, models, optimizers, Sequential
import nltk
import re

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from spacy import lemmatizer


def load_dataset(filename):
    df = pd.read_csv(filename, encoding="latin1",names=["Sentence", "Intent"])
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


def padding_doc(encoded_doc,max_length):
  return(pad_sequences(encoded_doc, maxlen = max_length,
                        padding =   "post"))

output_tokenizer = create_tokenizer(unique_intent,
                        filters = '!"#$%&()*+,-/:;<=>?@[\]^`{|}~')


def one_hot(encode):
    o = OneHotEncoder(sparse=False)
    return (o.fit_transform(encode))


train_X, val_X, train_Y, val_Y = train_test_split(padded_doc,output_one_hot, shuffle=True, test_size=0.2)


def create_model(vocab_size, max_length):
    model = Sequential()

    model.add(Embedding(vocab_size, 128,
                        input_length=max_length, trainable=False))
    model.add(Bidirectional(GRU(128)))
    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.5))
    model.add(BatchNormalization())
    model.add(Dense(21, activation="softmax"))

    return model


def predictions(text):
    clean = re.sub(r'[^ a-z A-Z 0-9]', " ", text)
    test_word = word_tokenize(clean)
    test_word = [lemmatizer.lemmatize(w.lower()) for w in test_word]
    test_ls = word_tokenizer.texts_to_sequences(test_word)

    # Check for unknown words
    if [] in test_ls:
        test_ls = list(filter(None, test_ls))

    test_ls = np.array(test_ls).reshape(1, len(test_ls))

    x = padding_doc(test_ls, max_length)

    pred = model.predict_classes(x)
    return pred


# map an integer to a word
def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None


text = "Can you help me?"
pred = predictions(text)
word = word_for_id(pred, output_tokenizer)