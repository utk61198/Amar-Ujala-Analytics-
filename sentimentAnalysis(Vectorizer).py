from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn import model_selection,preprocessing,linear_model,naive_bayes,metrics,svm
from sklearn import decomposition,ensemble
import pandas,xgboost,numpy,textblob,string
from keras.preprocessing import text,sequence

import settings
input=input("text")
def getTheData():
    with open(settings.DATA_FILE,"r") as text_file:
        data=text_file.read().split("\n")
        return data

def dataPreprocessing():
    preprocessed_data=[]
    for single_line in getTheData():
        if(len(single_line.split("\t"))==2 and single_line.split("\t")[1]!=""):
            preprocessed_data.append(single_line.split("\t"))
    return preprocessed_data

def splitData(data):
    total_length=len(data)
    training_ratio=0.8
    training_data=[]
    evaluation_data=[]
    for index in range(0,total_length):
        if(index<=total_length*training_ratio):
            training_data.append(data[index])
        else:
            evaluation_data.append(data[index])
    return training_data,evaluation_data

def getPreprocessedData():
    return splitData(dataPreprocessing())


def trainingProcess(data,vectorizer):
    training_text=[index[0] for index in data]
    training_result=[index[1] for index in data]
    training_text=vectorizer.fit_transform(training_text)
    return BernoulliNB().fit(training_text,training_result)

def printSentiment():
    training_data,evaluation_data=getPreprocessedData()
    vectorizer=CountVectorizer(binary="true")
    analyzer=trainingProcess(training_data,vectorizer)
    sentiment=analyzer.predict(vectorizer.transform([input]))
    if(sentiment[0]=='1'):
        print("positive sentiment")
    else:
        print("negative sentiment")
printSentiment()













