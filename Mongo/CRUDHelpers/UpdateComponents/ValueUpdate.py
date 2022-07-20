#Updates a field to contain the current date
def buildCurrentDateUpdate(field):
    updateObject = {"$currentDate" : {field : {"$type" : "date"}}}
    return updateObject
#Updates a field to contain the current time
def buildCurrentTimeUpdate(field):
    updateObject = {"$currentDate" : {field : {"$type" : "timestamp"}}}
    return updateObject
#Increments a field by a specified value
def buildIncrementUpdate(field, value):
    updateObject = {"$inc" : {field : value}}
    return updateObject
#Updates the value to be the lesser of the current value and the passed value (applies a minimum operation)
def buildMinimumUpdate(field, value):
    updateObject = {"$min" : {field : value}}
    return updateObject
#Updates the value to be the greater of the current value and the passed value (applies a maximum operation)
def buildMaximumUpdate(field, value):
    updateObject = {"$max" : {field : value}}
    return updateObject
#Multiplies the value of a field by a number
def buildMultiplyUpdate(field, value):
    updateObject = {"$mul" : {field : value}}
    return updateObject
#Changes the name of the current field to be the passed field name
def buildRenameUpdate(field, value):
    updateObject = {"$rename" : {field : value}}
    return updateObject
#Replaces the value of a field with the specified value
def buildSetUpdate(field, value):
    updateObject = {"$set" : {field : value}}
    return updateObject
#Deletes a particular field
def buildUnsetUpdate(field):
    updateObject = {"$unset" : {field : ""}}
    return updateObject