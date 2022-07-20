#Leaving a lot of this blank for now because I still want to think about how this should function

def updateSingleItem(collection, query, update, timeout):

    writeConcernObject = {"wtimeout": timeout}
    updateResult = collection.update_one(query, update, writeConcernObject)
    return updateResult


def updateMultipleItems(collection, query, update, timeout):

    writeConcernObject = {"wtimeout": timeout}
    updateResult = collection.update_many(query, update, writeConcernObject)
    return updateResult