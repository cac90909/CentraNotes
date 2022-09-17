import Util.Logging

#Retrieves the entire set of data that corresponds to a user id
#NOTE: this gets ALL data associated with a userid, including both the "data" and "metadata" field
def RetrieveUserData(userid, collection):
    try:
        userData = list(collection.find({"_id": userid}, {}))
        print("User data, for user with id ", userid, " has been found. Data: ")
        Util.Logging.PrettyPrintData(userData)
    except Exception as e:
        print("Error findind user data. Exception: ", e)
    return userData