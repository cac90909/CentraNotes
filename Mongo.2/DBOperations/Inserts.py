import Util.Users

#Gets the current number of users, increments by one, and then inserts a new document into the passed collection with the increment user id
#Also counts the number of document pre-creation and post-creation
def InsertNextUser(collection):
    try:
        numUsers = Util.Users.getUserCount(collection)
        nextUserNumber = numUsers + 1
        nextUserID = "user" + str(nextUserNumber)
        collection.insert_one({"_id" : nextUserID, "data" : None, "metadata" : None})
        newNumUsers = Util.Users.getUserCount(collection)
        print("Inserted Next User into collection. Previous number of users: ", numUsers, ". New number of users: ", newNumUsers)
    except Exception as e:
        print("Error inserting new user. Exception: ", e)
        
def CreateNewField(userid, field): pass

def CreateNewFieldWithValue(userid, field, value): pass