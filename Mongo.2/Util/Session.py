import pymongo

#Steps to starting a session:
    #1. Get the Mongo Client URI
    #2. Create instance of pyMongo client (this is probably a wrapper that start the Mongo Cluster by using the URI)
    #3. Open the appropriate database (currently this db is 'userdata')
    #4. Choose the appropriate collection (ex: 'user1')


def getMongoClientURI():
    with open(r"C:\Users\Chris\Desktop\mongoURI.txt") as f:
        mongoURI = f.readlines()[0]
    return mongoURI

def getMongoClient(mongoURI):
    mongoClient = pymongo.MongoClient(mongoURI)
    return mongoClient

def getMongoDatabase(mongoClient, databaseName="userdata"):
    database = mongoClient[databaseName]
    return database

def getMongoCollection(database, collectionName="main"):
    collection = database[collectionName]
    return collection

####################################

#Combines the above functions to start a Mongo Collection Session
def startMongoCollectionSession(collectionName="allusers", databaseName="userdata"):
    mongoURI = getMongoClientURI()
    mongoClient = getMongoClient(mongoURI)
    database = getMongoDatabase(mongoClient, databaseName)
    collection = getMongoCollection(database, collectionName)
    return collection

#Only starts the mongo database (ex: "userdata"), not a specific collection inside of the database
#NOTE: Im not sure if there will be a use case for just having the database session active, but making this function anyways
def startMongoDatabaseSession(databaseName="userdata"):
    mongoURI = getMongoClientURI()
    mongoClient = getMongoClient(mongoURI)
    database = getMongoDatabase(mongoClient, databaseName)
    return database

#This will end all server sessions created by this client, close all socketrs in the connection polls and stop the monitor threads, and cleanup client resources and disconnect from mongo DB
def endMongoSession(mongoClient):
    mongoClient.close()