import pymongo

#Steps to starting a session:
    #1. Get the Mongo Client URI
    #2. Start the Mongo Cluster by using the URI
    #3. Open the appropriate database (currently this db is 'userdata')
    #4. Choose the appropriate collection (ex: 'user1')


def getMongoClientURI():
    with open(r"C:\Users\Chris\Desktop\mongoURI.txt") as f:
        mongoURI = f.readlines()[0]
    return mongoURI

def getMongoCluster(mongoURI):
    clusterObject = pymongo.MongoClient(mongoURI)
    return clusterObject

def getMongoDatabase(clusterObject, databaseName = "userdata"):
    databaseObject = clusterObject[databaseName]
    return databaseObject

def getMongoCollection(databaseObject, collectionName):
    collectionObject = databaseObject[collectionName]
    return collectionObject

####################################

#Combines the above functions to start a Mongo Collection Session
def startMongoCollectionSession(collectionName, databaseName = "userdata"):
    mongoURI = getMongoClientURI()
    clusterObject = getMongoCluster(mongoURI)
    databaseObject = getMongoDatabase(clusterObject, databaseName)
    collectionObject = getMongoCollection(databaseObject, collectionName)
    return collectionObject

#This function is a business layer wrapper for the startMongoCollectionSession function (I may move this to go in a different python file)
#NOTE: userIDs correspond to the name of the mongo collection
def startMongoUserSession(userID, databaseName = "userdata"):
    userMongoSession = startMongoCollectionSession(databaseName = databaseName, collectionName = userID)
    return userMongoSession

#Only starts the mongo database (ex: "userdata"), not a specific collection inside of the database
def startMongoDatabaseSession(databaseName = "userdata"):
    mongoURI = getMongoClientURI()
    clusterObject = getMongoCluster(mongoURI)
    databaseObject = getMongoDatabase(clusterObject, databaseName)
    return databaseObject