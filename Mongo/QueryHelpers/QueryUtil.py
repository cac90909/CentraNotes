#Utility functions that assist in the building of queries. The following options are available: combining queries, adding a field to a query, getting a function from a passed operator
#NOTE: this file serves as barrier between QueryBuilder and Base.Query/Base.ArrayQuery
import QueryComponents.ValueQuery
import QueryComponents.ListQuery
import QueryComponents.QueryLogic

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

#Given an explict passed operator, will get the corresponding function that utilizes the mongo db equivalent operator
def getBaseQueryFromOperator(operator, value=None, valuesList=None):
    if operator == "=":
        return QueryComponents.ValueQuery.buildEqualsQuery(value)
    if operator == "!=":
        return QueryComponents.ValueQuery.buildNotEqualsQuery(value)
    if operator == ">":
        return QueryComponents.ValueQuery.buildGreaterThanQuery(value)
    if operator == ">=":
        return QueryComponents.ValueQuery.buildGreaterThanOrEqualsQuery(value)
    if operator == "<":
        return QueryComponents.ValueQuery.buildLessThanQuery(value)
    if operator == "<=":
        return QueryComponents.ValueQuery.buildLessThanOrEqualsQuery(value)
    if operator == "e":
        return QueryComponents.ValueQuery.buildExistsQuery()
    if operator == "!e":
        return QueryComponents.ValueQuery.buildNotExistsQuery()
    if operator == "in":
        return QueryComponents.ListQuery.buildInsideOfQuery(valuesList)
    if operator == "!in":
        return QueryComponents.ListQuery.buildNotInsideOfQuery(valuesList)
    if operator == "all":
        return QueryComponents.ListQuery.buildMatchAllQuery(valuesList)

#Given an explicitly passed operator, will add the corresponding logic to the list of queries/single query
def addLogicFromOperator(operator, query=None, queryList=None):
    if operator == "not":
        return QueryComponents.QueryLogic.addNotLogicToQuery(query)
    #Not and element match might be out of place here because and or and nor will follow similar syntaxes
    if operator == "em":
        return QueryComponents.QueryLogic.addElementMatchLogicToQuery(queryList)
    if operator == "and":
        return QueryComponents.QueryLogic.addAndLogicToQuery(queryList)
    if operator == "or":
        return QueryComponents.QueryLogic.addOrLogicToQuery(queryList)
    if operator == "nor":
        return QueryComponents.QueryLogic.addNorLogicToQuery(queryList)
    