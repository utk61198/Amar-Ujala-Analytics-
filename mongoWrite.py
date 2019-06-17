from pymongo import MongoClient
import SVO
import settings
import pymongo
import sentimentAnalysis
from copy import deepcopy
try:
    client=MongoClient(settings.DB_HOST_MONGO,username=settings.DB_USERNAME_MONGO,password=settings.DB_PASSWORD_MONGO)
    print("Connection Successfull")
except:
    print("connection unsuccessfull")

database=client[settings.DB_DATABASE_MONGO]
collection=database[settings.DB_COLLECTION_MONGO]
news_list=collection.find({},{"_id":1,"slug":1,"title":1,"synopsis":1})
news_list.sort("_id",pymongo.DESCENDING)

try:
    local_client=MongoClient(settings.DB_HOST_LOCAL)
    print("Connection successfull")
except:
    print("connection unsuccessfull")

local_database=local_client[settings.DB_DATABASE_LOCAL]
local_collection=local_database[settings.DB_COLLECTION_LOCAL]

def databaseInsert():
 for documents in range(25):
    inserting_document={}
    id_field=news_list[documents].get("_id")
    slug_field=news_list[documents].get("slug")
    synopsis_field=news_list[documents].get("synopsis")
    title_field=news_list[documents].get("title")
    sentimentAnalysis.text=title_field
    sentiment_score=sentimentAnalysis.getSentimentScore()
    sentiment_field="positive" if sentiment_score=="1" else "negative"
    subject_list, verb_list, object_list = deepcopy(SVO.initialRun(title_field))

    inserting_document["_id"]=id_field
    inserting_document["slug"]=slug_field
    inserting_document["title"]=title_field
    inserting_document["synopsis"]=synopsis_field
    inserting_document["sentiment"]=sentiment_field
    inserting_document["subject"]=subject_list
    inserting_document["verb"]=verb_list
    inserting_document["object"]=object_list
    local_collection.insert_one(inserting_document)

databaseInsert()











