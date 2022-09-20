import DBOperations.Finds

#TODO: think about if this verification is correct and if it belongs here. Should there be another method that deletes and verifies? Like it calls this method to delete and it verfies on its own.
def DeleteUser(collection, userId): 
    try:
        print("DBOperations.Deletes.DeleteUser")
        print("Attempting to delete ", userId, ".")
        print("First, verifying that user with id ", userId, " currently exists.")
        userData = DBOperations.Finds.FindUserData(userId, collection)
        if len(userData > 0):
            collection.delete_one({"_id": userId})
            print("Deletion is complete. Now going to verify its success.")
            newUserData = DBOperations.Finds.FindUserData(userId, collection)
            if len(newUserData == 0):
                print("Deletion was successful. Verified that user with id ", userId, " has the following empty data: ", newUserData)
            elif len(newUserData > 0):
                print("Deletion was not successful. User with id ", userId, " still has the following data: ", newUserData)
        elif len(userData == 0):
            print("The user intended to be deleted does not exist in the database.")
    except Exception as e:
        print("Error deleting ", userId, ". Exception: ", e)

#TODO: before the deletion check if the field exists, and after the deletion check/log if the field exists. This is the verification method to see if this method work
def DeleteField(collection, userId, field, value): 
    try:
        print("DBOperations.Deletes.DeleteField")
        print("Attempting to delete ", field, " for ", userId, ".")
        #print("First, verifying that user with id ", userId, " currently exists and possess the field ", field, " with value ", value)
        collection.update_one({"_id":userId}, {"$pull" : {field : value}})
        print("Deletion is complete.")
    except:
        print("Error deleting ", field, " for ", userId, ".")



#TODO
#Bulk delete on array of objects (ex: all objects in the array have a "age" field. Want the ability to bulk delete all of their age fields)  
#Conditional delete?
#Just delete the value of something not the field (aka set the value to None)