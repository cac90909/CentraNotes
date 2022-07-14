import Query

#Current idea for structuring of database items: (_id: <id>, data: <data>, metadata: <metadata>)

#Insertions
def insertItem(collection, id, dataItem, metadataItem):
    insertionObject = {"_id" : id, "data" : dataItem, "metadata" : metadataItem}
    result = collection.insert_one(insertionObject)
    print("API call received:", result.acknowledged)

def insertSubItem(collection): #Need to specify not only the item to be inserted/deleted, but also the nesting level
    pass

#Selections
def selectItem(collection):
    baseQuery = Query.buildBaseQuery("_id", None, id)
    result = collection.find_one(baseQuery)
def selectSubItem(id, path):
    pass
def selectSubItemConditionally(id, path, filter, filterValue):
    pass 

#Deletions
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
def updateItem(collection):
    pass
def updateItemConditionally(collection, id, path, filter):
    pass
 








