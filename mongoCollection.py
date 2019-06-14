
from pymongo import MongoClient
import pymongo
import settings

try:
   client=MongoClient(settings.DB_HOST_MONGO,username=settings.DB_USERNAME_MONGO,password=settings.DB_PASSWORD_MONGO)
   print("connection successfull")
except:
   print("Connection unsuccessfull")




database=client[settings.DB_DATABASE_MONGO]

def check(database_name):
     dblist=client.list_database_names()
     print(len(dblist))
     for str in dblist:
          	print(str)
     if database in dblist:
        print("database exixts")

#check(mydatabase)

collection_list=database.list_collection_names()
collection=database[settings.DB_COLLECTION_MONGO]

cursor=collection.find()
cursor.sort("_id",pymongo.DESCENDING)

count=0

news_list=[]

for documents in range(50):
    print(cursor[documents])
    news_list.append(cursor[documents])

    print("/n")
    count = count+1
print(news_list)































