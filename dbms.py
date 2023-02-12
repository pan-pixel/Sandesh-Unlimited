import pymongo
from datetime import datetime
from time import sleep

client = pymongo.MongoClient(
    "mongodb+srv://hackBnB:4uSfnWFb0Gn5PbaP@cluster0.x75vpnt.mongodb.net/?retryWrites=true&w=majority"
)

db = client["SandeshUnlimited"]


def sch_mail(time, sub, body, reCheck):
    collection = db["sch_mail"]
    val = {"time": time, "sub": sub, "body": body, "reCheck": reCheck}
    collection.insert_one(val)


def loginHandle(user, password):
    collection = db["users"]
    res = collection.find_one({"email": user}, {"password": 1, "_id": 0})
    if res != None:
        if res["password"] == password:
            return True
        else:
            return False
    else:
        return False
