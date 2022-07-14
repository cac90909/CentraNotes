#Projection: The projection parameter determines which fields are returned in the matching documents.
#NOTE: exclusion fields should be an array of attributes that are meant to not be returned, as indicated by the projection statement
    #Transforms: ["fieldName", "person.name.last", birthDate] -> {"fieldName":0, "person.name.last":0, birthDate: 0}
    #NOTE: all other field would be returned in the above projection statement. Only fields explicitly excluded are excluded
    #Inclusion works in the opposite way
    #You either pass this function an inclusion list OR an exlusion list, not both. The parameter not passed should be none
#TODO: incorporate more projeciton functionalities to allow for more options for projections and returned db values
def buildBaseProjection(inclusionFields, exclusionFields):
    if inclusionFields is None:
        return {field : 0 for field in exclusionFields}
    if exclusionFields is None:
        return {field : 0 for field in inclusionFields}


