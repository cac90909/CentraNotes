#Official Mongo DB Delete Documentation: https://www.mongodb.com/docs/manual/reference/method/db.collection.deleteOne/

def deleteSingleItem(collection, query, timeout):

    writeConcernObject = {"wtimeout": timeout}
    deleteResult = collection.delete_one(query, writeConcernObject)
    return deleteResult

def deleteMultipleItems(collection, query, timeout):

    writeConcernObject = {"wtimeout": timeout}
    deleteResult = collection.delete_many(query, writeConcernObject)
    return deleteResult