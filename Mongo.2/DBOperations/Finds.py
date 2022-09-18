import Util.Logging

#Retrieves the entire set of data that corresponds to a user id
#NOTE: this gets ALL data associated with a userid, including both the "data" and "metadata" field
def FindUserData(userid, collection):
    try:
        userData = list(collection.find({"_id": userid}, {}))
        print("User data, for user with id ", userid, " has been found. Data: ")
        Util.Logging.PrettyPrintData(userData) 
        return userData
    except Exception as e:
        print("Error findind user data. Exception: ", e)
    

#Does not retrieve the entire set of user data, but rather a specified field
#NOTE: currently this also grabs the layers preceding the passed field. Can change this if I need to later
def FindDataField(userid, collection, field):
    try:
        #Setting the projection to be {field:1} means the only thing returned is the specified field
        data = list(collection.find({"_id": userid}, {"_id" : 0, field: 1}))
        print("Data retrieval complete - DBOperations.Finds.FindDataField()")
        print("Field: ", field)
        print("Value: ")
        Util.Logging.PrettyPrintData(data)
        return data
    except Exception as e:
        print("Error finding the field with given value. Exception: ", e)