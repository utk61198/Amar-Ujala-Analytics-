from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn import model_selection,preprocessing,linear_model,naive_bayes,metrics,svm
from sklearn import decomposition,ensemble
import pandas,xgboost,numpy,textblob,string
from keras.preprocessing import text,sequence
import settings

text=""
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

training_data,evaluation_data=getPreprocessedData()
vectorizer=CountVectorizer(binary="true")
analyzer=trainingProcess(training_data,vectorizer)
def getSentimentScore():
     sentiment=analyzer.predict(vectorizer.transform([text]))
     return sentiment[0]

def printSentiment(sentiment):
    if(sentiment=='1'):
        print("positive sentiment")
    else:
        print("negative sentiment")

def evaluationFuntion(evaluation_data):
    evaluation_text=[evaluation_data[0] for evaluation_data in evaluation_data]
    evaluation_result=[evaluation_data[1] for evaluation_data in evaluation_data]
    total_len=len(evaluation_text)
    correct_ans=0
    for index in range(0,total_len):
        sentiment=analyzer.predict(vectorizer.transform([evaluation_text[index]]))
        if(sentiment[0]==evaluation_result[index]):
            correct_ans=correct_ans+1
        else:
            correct_ans=correct_ans+0
    accuracy=(correct_ans*100)/total_len

    return accuracy














