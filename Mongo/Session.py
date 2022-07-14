import pymongo

#Reads in the Mongo DB URI ->
#Connects to cluster using the URI + MongoClient
#Connects "userdata" database using the cluster
#Connects to "user1" collection using the "userdata" database
#TODO: want to add later customization for connecting to different databases and different collections
#NOTE: for current test purposes all data is in the "user1" collection located in "userdata" database
def StartMongoSession():

    with open(r"C:\Users\Chris\Desktop\mongoURI.txt") as f:
        mongoURI = f.readlines()[0]

    cluster = pymongo.MongoClient(mongoURI)
    db = cluster["userdata"]
    collection = db['user1']

    return collection