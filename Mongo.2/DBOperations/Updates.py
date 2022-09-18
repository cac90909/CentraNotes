import DBOperations.Finds

def UpdateUserID(oldUserId, newUserId): pass

#Changes a name of a field.
#NOTE: I believe this only allows for a singular update
#TODO: I want to expand on this to allow for a bulk update (example, changing a list of objects that all have the same parameters, but changing one of those parameters names for all of the objects in the list)
def UpdateFieldName(collection, userId, oldFieldName, newFieldName):
    try:
        print("Field-Value pairing prior to the name update:")
        DBOperations.Finds.FindDataField(userId, collection, oldFieldName)
        collection.update_one({"_id" : userId}, {"$rename" : {oldFieldName: newFieldName}}, False, False) #First false is for upsert parameter and second false is for multi update
        print("Update complete. Field-Value pairing after the name update:")
        DBOperations.Finds.FindDataField(userId, collection, newFieldName)
    except Exception as e:
        print("Error updating the field name. Exception: ", e)

#For changing the value of a field or creating a new field
#NOTE: when creating a new field, you can have an empty value if you pass "None" as the value parameter of this function 
#NOTE: I believe this only allows for a singular update
#TODO: I want to expand on this to allow for a bulk update (see above example for the udpate field name function)
def UpdateFieldWithValue(collection, userId, field, value):
    try:
        print("Field-Value pairing prior to the update:")
        DBOperations.Finds.FindDataField(userId, collection, field)
        collection.update_one({"_id" : userId}, {"$set" : {field: value}})
        print("Update complete. Field-Value pairing after the update:")
        DBOperations.Finds.FindDataField(userId, collection, field)
    except Exception as e:
        print("Error inserting new user. Exception: ", e)



#Use Case for adding a value to an existing array data structure
def UpdateFieldWithAdditionalValue(userId, field, value): pass