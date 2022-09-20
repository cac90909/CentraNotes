import DBOperations.Finds

#Changes a name of a field (singular update)
#NOTE: I believe this only allows for a singular update
def UpdateFieldName(collection, userId, oldFieldName, newFieldName):
    try:
        print("DBOperations.Updates.UpateFieldName")
        print("Field-Value pairing prior to the name update:")
        DBOperations.Finds.FindDataField(userId, collection, oldFieldName)
        collection.update_one({"_id" : userId}, {"$rename" : {oldFieldName: newFieldName}}, False, False) #First false is for upsert parameter and second false is for multi update
        print("Update complete. Field-Value pairing after the name update:")
        DBOperations.Finds.FindDataField(userId, collection, newFieldName)
    except Exception as e:
        print("Error updating the field name. Exception: ", e)


#For changing the value of a field or creating a new field
#NOTE: when creating a new field, you can have an empty value if you pass "None" as the value parameter of this function 
#NOTE: To update a nested field, use the dot operator. Example: "myField.nestedField.anotherNestedField". Example of nested array field: "myField.myNestedArray.2.color" (the 2 specifies the 2nd element of 'myNestedArray')
def UpdateFieldValue(collection, userId, field, value):
    try:
        print("DBOperations.Updates.UpdateFieldValue")
        print("Field-Value pairing prior to the update:")
        DBOperations.Finds.FindDataField(userId, collection, field)
        collection.update_one({"_id" : userId}, {"$set" : {field: value}})
        print("Update complete. Field-Value pairing after the update:")
        DBOperations.Finds.FindDataField(userId, collection, field)
    except Exception as e:
        print("Error inserting new user. Exception: ", e)

#TODO:
#Bulk update field names (ex: update a field that exists in the objects held in an array)
#Bulk update field values
#Re-calibrate user ids (making sure user ids go 1->2->3->etc.)