import Util.Logging

#Retrieves the entire set of data that corresponds to a user id
#NOTE: this gets ALL data associated with a userid, including both the "data" and "metadata" field
def FindUserData(userid, collection):
    try:
        print("DBOperations.Finds.FindUserData")
        userData = list(collection.find({"_id": userid}, {}))
        print("User data, for user with id ", userid, " has been found. Data: ")
        Util.Logging.PrettyPrintData(userData) 
        return userData
    except Exception as e:
        print("Error findind user data. Exception: ", e)
    

#Does not retrieve the entire set of user data, but rather a specified field
#NOTE: however, at the passed level if there are multiple objects (example: an array of objects), then all objects will be return, unless you specify the object to be returned
#NOTE: currently this also grabs the layers preceding the passed field. Can change this if I need to later
def FindDataField(userid, collection, field):
    try:
        print("DBOperations.Finds.FindDataField")
        #Setting the projection to be {field:1} means the only thing returned is the specified field
        data = list(collection.find({"_id": userid}, {"_id" : 0, field: 1}))
        print("Data retrieval complete.")
        print("Field: ", field)
        print("Value: ")
        Util.Logging.PrettyPrintData(data)
        return data
    except Exception as e:
        print("Error finding the field with given value. Exception: ", e)

#TODO
#Do I need another find for arrays?
#Do I need more finds to verify other CRUD operations