#Matches values that are equal to a specified value.
def buildEqualsQuery(value):
    return {"$eq" : value}
#Matches all values that are not equal to a specified value.
def buildNotEqualsQuery(value):
    return {"$ne" : value}
#Matches values that are greater than a specified value.
def buildGreaterThanQuery(value):
    return {"$gt" : value}
#Matches values that are greater than or equal to a specified value.
def buildGreaterThanOrEqualsQuery(value):
    return {"$gte" : value}
#Matches values that are less than a specified value.
def buildLessThanQuery(value):
    return {"$lt" : value}
#Matches values that are less than or equal to a specified value.
def buildLessThanOrEqualsQuery(value):
    return {"$lte" : value}
#when applying the exists operator, it will only return a document/sub-document if the specified field exists (it can have ANY value, just has to exist)
def buildExistsQuery():
    return {"$exists" : True}
#when applying the exists operator, it will only return a document/sub-document if the specified field exists (it can have ANY value, just has to exist)
def buildNotExistsQuery():
    return {"$exists" : False}
#Matches any of the values specified in an array.
def buildInsideOfQuery(valuesList):
    return {"$in" : valuesList}
#Matches none of the values specified in an array.
def buildNotInsideOfQuery(valuesList):
    return {"$nin" : valuesList}
#selects the documents where the value of a field is an array that contains all the specified elements.
def buildMatchAllQuery(valuesList):
    return {"$all" : valuesList}

#performs a logical NOT operation on the specified <operator-expression> and selects the documents that do not match the <operator-expression>
def addNotLogicToQuery(query):
    return {"$not" : query}
#he $elemMatch operator matches documents that contain an array field with at least one element that matches all the specified query criteria.
def addElementMatchLogicToQuery(queryList):
    return {"$elemMatch" : queryList}
#queryList must be of type list
#performs a logical AND operation on an array of one or more expressions
def addAndLogicToQuery(queryList):
    return {"$and" : queryList}
#Logical OR operation on an array of two or more expressions and selects the documents that satisfy at least one of the expressions
def addOrLogicToQuery(queryList):
    return {"$or" : queryList}
#performs a logical NOR operation on an array of one or more query expression and selects the documents that fail all the query expressions in the array.
def addNorLogicToQuery(queryList):
    return {"$nor" : queryList}
#combines the query dictionary objects passed. Input should be of type list
def combineQueries(queryList):
    baseQuery = queryList[0]
    for query in queryList[1:]:
        baseQuery.update(query)
    combinedQueries = baseQuery
    return combinedQueries
    
#This function is going to probably be used in all query creations
def addFieldToQuery(field, query):
    return {field : query}








        




#TODO: make an array query builder
#TODO: think about how in the future you can make query building more scalable (if we make everything into a function, but the combinations of queries are high, this means a lot of function building in the future
#but having a single or a couple custom array building functions would solve a similar trick)
#Example: passing into the function a list representing the query. Here: [{,"height","greaterThan",5,}] -> Every part of the query is passed in by a list. This is just one implementation thought
mongoQueryArrayOperators = { "all" : "$all", #The $all operator selects the documents where the value of a field is an array that contains ALL the specified elements (order does not matter though)
                        "elementMatch" : "$elemMatch" #The $elemMatch operator matches documents that contain an array field with at least one element that matches all the specified query criteria.

}


