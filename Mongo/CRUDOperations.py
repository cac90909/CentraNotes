import QueryBuilder
import pymongo
import CRUDHelpers.DeleteUtil

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
mongoUnsetOperator = "$unset"
def deleteItem(collection, id):
    deletionObject = {"_id" : id}
    result = collection.delete_one(deletionObject)
    print("API call recieved:", result.acknowledged)
    print("Documents deleted:", result.deleted_count)

def deleteSubItem(collection):
    pass

def deleteSubItemConditionally(collection):
    pass

#Updates
mongoSetOperator = "$set"
def updateItem(collection, id, path, value):
    filterObject = {"_id" : id}
    updateObject = {mongoSetOperator : {path : value}}
    collection.update_one(filterObject, updateObject)
#TODO: come up with way to facilitate creation of filter objects
def updateItemConditionally(collection, id, path, filter, value):
    filterObject = {"_id" : id}
    filterObject.update(filter) #This merges the two dict objects into one
    updateObject= { mongoSetOperator : { path : value}}
    collection.update(filterObject, updateObject, upsert=True, multi=True)
 







#Timeout is in milliseconds
#NOTE: might converge these into a single delete method that has a parameter so you specify you want to delete single item or multiple item
def deleteSingleItem(collection, query, timeout):

        deleteResult = CRUDHelpers.DeleteUtil.deleteSingleItem(collection, query, timeout)
        deleteSuccess = deleteResult[0]
        deletedItems = deleteResult[1]

def deleteSingleItem(collection, query, timeout):

        deleteResult = CRUDHelpers.DeleteUtil.deleteMultipleItems(collection, query, timeout)
        deleteSuccess = deleteResult[0]
        deletedItems = deleteResult[1]



