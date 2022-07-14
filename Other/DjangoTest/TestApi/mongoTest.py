import pymongo

mongoPass = "MkqSTZMiOd65DcsV"


cluster = pymongo.MongoClient("mongodb+srv://cac909:MkqSTZMiOd65DcsV@centranotescluster.ij4jgvq.mongodb.net/?retryWrites=true&w=majority")
db = cluster["userdata"]
collection = db['user1']

#collection.insert_one({"_id" : 16, "data" : [[1,2,3],[1,2,3],[1,2,3],20, {"random" : "yes"}]})

#import mongoengine
#mongoengine.connect(db="userdata", host="localhost", username="cac909", password="MkqSTZMiOd65DcsV")

#End points I want:

#Type Check ID? Since it can only be string or int
def selectAllCollectionDocuments():
    collection.find()


#Inserting single item
#NOTE: I dont think I need to use collection.insert_many since all of my data is structured like (_id: <id>, data: <data>). Which means I am only ever going to be inserting or updating or selecting things from one 
#document at a time since each document (row entry) corresponds to a single user. There really isn't much business context to be doing operations accross multiple users. Maybe from a devops perspective there is
#some use there, but that is further down the line. I am okay for now just having insert_one and delete_one, etc.
#TODO: these methods should be structure checking to maintain the (_id: <id>, data: <data>) structure
#TODO: might need to change method wording (naming) and variable naming if I want to have a business vs technical layer
#TODO: all these methods should probably have a try and catch mechanism implemented or something for error handling (ex: inserting item at an already existing id)
#TODO: I need to differentaiate and understand what I mean wwhen I say item vs subitem
def insertItem(id, dataItem, metadataItem):
    insertionObject = {"_id" : id, "data" : dataItem, "metadata" : metadataItem}
    result = collection.insert_one(insertionObject)
    print("API call received:", result.acknowledged)
#Inserting multiple items (a list of items)
#def insertMultipleItem(id, data):
#    collection.insert_many({"id":id, "data": data})
#Deleting single item
def deleteItem(id):
    deletionObject = {"_id" : id}
    result = collection.delete_one(deletionObject)
    print("API call recieved:", result.acknowledged)
    print("Documents deleted:", result.deleted_count)
#Deleting multiple items
#def deleteMultipleItem():
#    pass
#Inserting/Deleting nested items
def insertSubItem(): #Need to specify not only the item to be inserted/deleted, but also the nesting level
    pass
def deleteSubItem():
    pass
def deleteSubItemConditionally():
    pass
#Updating nested items (ex: updating value at top of the nesting and updating value at bottom of nesting)
def updateItem():
    pass
def updateItemConditionally(id, path, filter):
    pass
#Selecting entire row (by id)
def selectItem(id):
    baseQuery = MongoCRUDHelper.buildBaseQuery("_id", None, id)
    result = collection.find_one(baseQuery)
#Selecting custom subset of items (how to filter)
#NOTE: use this as reference: https://stackoverflow.com/questions/25586901/how-to-find-document-and-single-subdocument-matching-given-criterias-in-mongodb
#NOTE: path variable should incorporate the dot notation: https://www.mongodb.com/docs/manual/core/document/#dot-notation
def selectSubItem(id, path):
    pass
def selectSubItemConditionally(id, path, filter, filterValue):
    pass #NOTE: need to figure out the mechanism for filter
    #NOTE: selectSubItemConditionally might not be good because it is modularized function (it is combining getting sub item AND applying a condition) because functions should really only do one thing - right? or am i crazy here (a little high haha 4:47 AM)

#insertItem(id="user5", dataItem = {"days ": {"summer" : [30,31,35], "winter" : {"snow" : True}}}, metadataItem = {"creationDate" : "7/3/2022 2:32 AM"})
#deleteItem(id=12)




class MongoCRUDHelper:

    #Queries
    mongoQueryComparisonOperators = {"equals": "$eq", #Matches values that are equal to a specified value.
                        "greaterThan" : "$gt", #Matches values that are greater than a specified value.
                        "greaterThanOrEquals" : "$gte", #Matches values that are greater than or equal to a specified value.
                        "insideOf" : "$in", #Matches any of the values specified in an array.
                        "lessThan" : "$lt", #Matches values that are less than a specified value.
                        "lessThanOrEquals" : "$lte",#Matches values that are less than or equal to a specified value.
                        "notEquals" : "$ne", #Matches all values that are not equal to a specified value.
                        "notInsideOf" : "$nin", #Matches none of the values specified in an array.
                        }
    #Builds base of queries
    #NOTE: operator can be None to allow for a basic field=value query
    def buildQuery(field, value):
            return { field : value }
    def buildComparisonQuery(field, operator, value):
        return { field : { MongoCRUDHelper.mongoQueryComparisonOperators[operator] : value} }
    
    

    mongoQueryOtherOperators = { "not" : "$not", #$not performs a logical NOT operation on the specified <operator-expression> and selects the documents that do not match the <operator-expression> 
                        "exists" : "$exists" #when applying the exists operator, it will only return a document/sub-document if the specified field exists (it can have ANY value, just has to exist)
    }

    def buildNotQuery(field, value):
        return { field : { MongoCRUDHelper.mongoQueryOtherOperators["not"]  : value } } 
    def buildComparisonNotQuery(field, operator, value):
        return { field : { MongoCRUDHelper.mongoQueryOtherOperators["not"] : {MongoCRUDHelper.mongoQueryComparisonOperators[operator] : value } } }
    def buildExistsQuery(field):
        return { field : { MongoCRUDHelper.mongoQueryOtherOperators["exists"] : True } }
    def buildNotExistsQuery(field):
        return { field : { MongoCRUDHelper.mongoQueryOtherOperators["exists"] : False } }
            
    

    mongoQueryLogicalOperators = { "or" : "$or", #Logical OR operation on an array of two or more expressions and selects the documents that satisfy at least one of the expressions
                        "and" : "$and", #performs a logical AND operation on an array of one or more expressions
                        "nor" : "$nor"

    }

    #Adds logical operator in front of two or more queries
    def addLogicalOperator(operator, queryList):
        return { MongoCRUDHelper.mongoQueryLogicalOperators[operator] : queryList }


    #TODO: make an array query builder
    #TODO: think about how in the future you can make query building more scalable (if we make everything into a function, but the combinations of queries are high, this means a lot of function building in the future
    #but having a single or a couple custom array building functions would solve a similar trick)
    #Example: passing into the function a list representing the query. Here: [{,"height","greaterThan",5,}] -> Every part of the query is passed in by a list. This is just one implementation thought
    mongoQueryArrayOperators = { "all" : "$all", #The $all operator selects the documents where the value of a field is an array that contains ALL the specified elements (order does not matter though)
                            "elementMatch" : "$elemMatch" #The $elemMatch operator matches documents that contain an array field with at least one element that matches all the specified query criteria.

    }


    #Projection: The projection parameter determines which fields are returned in the matching documents.
    #NOTE: exclusion fields should be an array of attributes that are meant to not be returned, as indicated by the projection statement
        #Transforms: ["fieldName", "person.name.last", birthDate] -> {"fieldName":0, "person.name.last":0, birthDate: 0}
        #NOTE: all other field would be returned in the above projection statement. Only fields explicitly excluded are excluded
        #Inclusion works in the opposite way
        #You either pass this function an inclusion list OR an exlusion list, not both. The parameter not passed should be none
    #TODO: incorporate more projeciton functionalities to allow for more options for projections and returned db values
    def buildBaseProjection(inclusionFields, exclusionFields):
        if inclusionFields is None:
            return {field : 0 for field in exclusionFields}
        if exclusionFields is None:
            return {field : 0 for field in inclusionFields}
    

