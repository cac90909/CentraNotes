#Builds Base Array Query For the Following Operations: Some Values Match, No Values MAtch, All Values Match

#Matches any of the values specified in an array.
def buildInsideOfQuery(valuesList):
    return {"$in" : valuesList}
#Matches none of the values specified in an array.
def buildNotInsideOfQuery(valuesList):
    return {"$nin" : valuesList}
#selects the documents where the value of a field is an array that contains all the specified elements.
def buildMatchAllQuery(valuesList):
    return {"$all" : valuesList}