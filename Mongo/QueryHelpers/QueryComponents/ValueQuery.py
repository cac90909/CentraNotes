#Builds Base Query for the following operations: Equals, Not Equals, Greater Than, Greater Than or Equals, Less Than, Less Than or Equals, Exists, Does Not Exist

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