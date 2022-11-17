from pymongo import *
mycli=MongoClient("mongodb://localhost:27017")
mydba=mycli['ACs']
mytba=mydba["list"]

for i in mytba.find():
    print(i)