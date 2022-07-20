#Removes first element of a list
def buildRemoveFirstElementUpdate(field):
    updateObject = {"$pop" : {field : -1}}
    return updateObject
#Removes last element of a list
def buildRemoveLastElementUpdate(field):
    updateObject = {"$pop" : {field : 1}}
    return updateObject
#Removes specified element from an array
#NOTE: $pull statement can also have a condition instead of value, but I figure the query will take of that condition so I did not implement an option to have a condition here
def buildRemoveElementUpdate(field, value):
    updateObject = {"$pull" : {field : value}}
    return updateObject
#Appends item at the end of a list
def buildPushSingleElementUpdate(field, value):
    updateObject = {"$push" : {field : value}}
    return updateObject
#Appends multiple items at the end of a list
def buildPushMultipleElementsUpdate(field, valuesList):
    updateObject = {"$push" : {field : { "$each" : valuesList}}}
    return updateObject
#Removes all matching elements from an array
def buildPullAllElementsUpdate(field, valuesList):
    updateObject = {"$pullAll" : {field : valuesList}}
    return updateObject
