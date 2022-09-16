import Util.MongoInfo

#This function counts the number of documents in the given collection. Each document corresponds to 1 users entire set of data, so number of documents = number of users
def getUserCount(collection):
    numUsers = Util.MongoInfo.getNumDocumentsInCollection(collection)
    return numUsers  

