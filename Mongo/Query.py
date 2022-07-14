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
    return { field : { mongoQueryComparisonOperators[operator] : value} }



mongoQueryOtherOperators = { "not" : "$not", #$not performs a logical NOT operation on the specified <operator-expression> and selects the documents that do not match the <operator-expression> 
                    "exists" : "$exists" #when applying the exists operator, it will only return a document/sub-document if the specified field exists (it can have ANY value, just has to exist)
}

def buildNotQuery(field, value):
    return { field : { mongoQueryOtherOperators["not"]  : value } } 
def buildComparisonNotQuery(field, operator, value):
    return { field : { mongoQueryOtherOperators["not"] : {mongoQueryComparisonOperators[operator] : value } } }
def buildExistsQuery(field):
    return { field : { mongoQueryOtherOperators["exists"] : True } }
def buildNotExistsQuery(field):
    return { field : { mongoQueryOtherOperators["exists"] : False } }
        


mongoQueryLogicalOperators = { "or" : "$or", #Logical OR operation on an array of two or more expressions and selects the documents that satisfy at least one of the expressions
                    "and" : "$and", #performs a logical AND operation on an array of one or more expressions
                    "nor" : "$nor"

}

#Adds logical operator in front of two or more queries
def addLogicalOperator(operator, queryList):
    return { mongoQueryLogicalOperators[operator] : queryList }


#TODO: make an array query builder
#TODO: think about how in the future you can make query building more scalable (if we make everything into a function, but the combinations of queries are high, this means a lot of function building in the future
#but having a single or a couple custom array building functions would solve a similar trick)
#Example: passing into the function a list representing the query. Here: [{,"height","greaterThan",5,}] -> Every part of the query is passed in by a list. This is just one implementation thought
mongoQueryArrayOperators = { "all" : "$all", #The $all operator selects the documents where the value of a field is an array that contains ALL the specified elements (order does not matter though)
                        "elementMatch" : "$elemMatch" #The $elemMatch operator matches documents that contain an array field with at least one element that matches all the specified query criteria.

}


