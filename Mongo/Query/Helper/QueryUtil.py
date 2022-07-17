#Utility functions that assist in the building of queries. The following options are available: combining queries, adding a field to a query

#combines the query dictionary objects passed. Input should be of type list
def combineQueries(queryList):
    baseQuery = queryList[0]
    for query in queryList[1:]:
        baseQuery.update(query)
    combinedQueries = baseQuery
    return combinedQueries

#This function is going to probably be used in all query creations
def addFieldToQuery(field, query):
    return {field : query}