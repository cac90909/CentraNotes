import Util.Users

#Gets the current number of users, increments by one, and then inserts a new document into the passed collection with the increment user id
#Also counts the number of document pre-creation and post-creation
def InsertNextUser(collection):
    numUsers = Util.Users.getUserCount(collection)
    nextUserNumber = numUsers + 1
    nextUserID = "user" + str(nextUserNumber)
    collection.insert_one({"_id" : nextUserID, "data" : None, "metadata" : None})
    newNumUsers = Util.Users.getUserCount(collection)
    print("Previous number of users: ", numUsers, ". New number of users: ", newNumUsers)

def CreateNewField(userid, field): pass

def CreateNewFieldWithValue(userid, field, value): pass