#Adds the following logical operations to an already existing list of queries or single query: element match, not, and, or, nor

#performs a logical NOT operation on the specified <operator-expression> and selects the documents that do not match the <operator-expression>
def addNotLogicToQuery(query):
    return {"$not" : query}
#he $elemMatch operator matches documents that contain an array field with at least one element that matches all the specified query criteria.
def addElementMatchLogicToQuery(queryList):
    return {"$elemMatch" : queryList}
#performs a logical AND operation on an array of one or more expressions
def addAndLogicToQuery(queryList):
    return {"$and" : queryList}
#Logical OR operation on an array of two or more expressions and selects the documents that satisfy at least one of the expressions
def addOrLogicToQuery(queryList):
    return {"$or" : queryList}
#performs a logical NOR operation on an array of one or more query expression and selects the documents that fail all the query expressions in the array.
def addNorLogicToQuery(queryList):
    return {"$nor" : queryList}