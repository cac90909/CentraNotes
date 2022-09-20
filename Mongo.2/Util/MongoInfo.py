#4 limitations to using .rename()
    #1: cannot move a collection between db's
    #2: cannot rename views
    #3: cannot be used on time series collections (I think there is another method for this)
    #4: cannot rename a collection to its current name
#NOTE: renaming the database can be done as well, but I think it may have a couple more steps than renaming a collection (as shown here)
#NOTE: if a collection already exists with the name you are trying to change to, then you have to add an additional dropTarget=True parameter on the rename call (currently this param is optional)
def RenameMongoCollection(collection, newName):
    print("Util.MongoInfo.RenameMongoCollection")
    collection.rename(new_name = newName)

#Retrieves the name jof all collections in a database and stores them in a list (to retrieve, you can just loop through the list)
#NOTE: must pass a database object
def GetCollectionNamesFromDatabase(database):
    print("Util.MongoInfo.GetCollectionNamesFromDatabase")
    collectionNames = database.collection_names()
    return collectionNames

#Counts the number of documents present in a mongo db collection
def GetNumDocumentsInCollection(collection):
    print("Util.MongoInfoGetNumDocumentsInCollection")
    numDocuments = collection.count_documents({})
    return numDocuments