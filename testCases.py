from pymongo import MongoClient
import pymongo
import settings
import SVO
import csv
from copy import deepcopy
try:
   client=MongoClient(settings.DB_HOST_MONGO,username=settings.DB_USERNAME_MONGO,password=settings.DB_PASSWORD_MONGO)
   print("connection successfull")
except:
   print("Connection unsuccessfull")

database=client[settings.DB_DATABASE_MONGO]
collection_list=database.list_collection_names()
collection=database[settings.DB_COLLECTION_MONGO]
cursor=collection.find()
cursor.sort("_id",pymongo.DESCENDING)
news_title_list = []
svo_list=()
def svoExtraction(str,writer):
    new_cursor=collection.find({},{str:1,"_id":0})
    new_cursor.sort("_id",pymongo.DESCENDING)
    heading_row=[["News Title","Subject","Verb","Object"]]
    writer.writerows(heading_row)
    for documents in range(100):

        for news_title in new_cursor[documents].values():
            news_title_list.append(news_title)


    for news_title in news_title_list:
        subject_list,verb_list,object_list=deepcopy(SVO.initialRun(news_title))

        svo_row = [[news_title,subject_list,verb_list,object_list]]

        writer.writerows(svo_row)
sampleFile=open('sample.csv','w')
writer=csv.writer(sampleFile)
svoExtraction("title",writer)
sampleFile.close()












