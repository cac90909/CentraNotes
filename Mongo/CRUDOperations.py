import QueryBuilder
import pymongo
import CRUDHelpers.DeleteUtil
import CRUDHelpers.UpdateUtil

#Current database item structure: (_id: <id>, data: <data>, metadata: <metadata>)

#Insertions
def insertItem(collection, id, dataItem, metadataItem):
    insertionObject = {"_id" : id, "data" : dataItem, "metadata" : metadataItem}
    result = collection.insert_one(insertionObject)
    print("API call received:", result.acknowledged)

def insertSubItem(collection): #Need to specify not only the item to be inserted/deleted, but also the nesting level
    pass

#Selections
def selectItem(collection, id):
    baseQuery = Query.buildQuery("_id", id)
    result = collection.find_one(baseQuery)
    return result
def selectSubItem(collection, id, path):
    #baseQuery = Query.buildQuery("_id", id)
    baseQuery = {"_id":id}
    baseProjection = {}
    result = collection.find_one(baseQuery)
    return result
def selectSubItemConditionally(id, path, filter, filterValue):
    pass 

#Deletions

#Timeout is in milliseconds
#NOTE: might converge these into a single delete method that has a parameter so you specify you want to delete single item or multiple item
def deleteSingleItem(collection, query, timeout):

    deleteResult = CRUDHelpers.DeleteUtil.deleteSingleItem(collection, query, timeout)
    deleteSuccess = deleteResult[0]
    deletedItems = deleteResult[1]

def deleteMultipleItems(collection, query, timeout):

    deleteResult = CRUDHelpers.DeleteUtil.deleteMultipleItems(collection, query, timeout)
    deleteSuccess = deleteResult[0]
    deletedItems = deleteResult[1]





#Updates

def updateSingleItem(collection, query, update, timeout):

    updateResult = CRUDHelpers.UpdateUtil.updateSingleItem(collection, query, update, timeout)
    updateSuccess = updateResult[0]
    updateItems = updateResult[1]

def updateMultipleItems(collection, query, update, timeout):

    updateResult = CRUDHelpers.UpdateUtil.updateMultipleItems(collection, query, update, timeout)
    updateSuccess = updateResult[0]
    updateItems = updateResult[1]



