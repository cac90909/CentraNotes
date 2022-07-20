#Deletes first element in list that matches condition (this function only builds the update object, not query (condition) object)
def buildFirstMatchingElementOperation(listField, value):
    concatField = listField + ".$"
    updateComponent = {concatField : value}
    return updateComponent
#indicates that the update operator should modify all elements in the specified array field
def buildAllMatchingElementsOperation(listField, value):
    concatField = listField + ".$[]"
    updateComponent = {concatField : value}
    return updateComponent
    