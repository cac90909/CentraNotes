#Utilizes the Query.Helper python files to make it easier to construct Mongo DB Query Objects
import QueryHelpers.QueryUtil


#comparisonOperator options include (strings): =, !=, >, >=, <, <=, e (exists), !e (does not exist), in (inside of), !in, all (match all)
def buildOneComparisonOneFieldQuery(field, comparisonOperator, value=None, valuesList=None):
    baseQuery = QueryHelpers.QueryUtil.getBaseQueryFromOperator(comparisonOperator, value, valuesList)
    completedQuery = QueryHelpers.QueryUtil.addFieldToQuery(field, baseQuery)
    return completedQuery

def buildTwoComparisonsOneFieldQuery(field, comparisonOperator1, comparisonOperator2, value1=None, valuesList1=None, value2=None, valuesList2=None):
    baseQuery1 = QueryHelpers.QueryUtil.getBaseQueryFromOperator(comparisonOperator1, value1, valuesList1)
    baseQuery2 = QueryHelpers.QueryUtil.getBaseQueryFromOperator(comparisonOperator2, value2, valuesList2)
    queryList = [baseQuery1, baseQuery2]
    combinedQuery = QueryHelpers.QueryUtil.combineQueries(queryList)
    completedQuery = QueryHelpers.QueryUtil.addFieldToQuery(field, combinedQuery)
    return completedQuery
    
#logicalOperator options include: and, or, nor
def buildTwoComparisonsTwoFieldQueryWithLogic(field1, field2, comparisonOperator1, comparisonOperator2, logicalOperator, value1=None, valuesList1=None, value2=None, valuesList2=None):
    baseQuery1 = QueryHelpers.QueryUtil.getBaseQueryFromOperator(comparisonOperator1, value1, valuesList1)
    baseQuery2 = QueryHelpers.QueryUtil.getBaseQueryFromOperator(comparisonOperator2, value2, valuesList2)
    baseQueryWithField1 = QueryHelpers.QueryUtil.addFieldToQuery(field1, baseQuery1)
    baseQueryWithField2 = QueryHelpers.QueryUtil.addFieldToQuery(field2, baseQuery2)
    queryList = [baseQueryWithField1, baseQueryWithField2]
    completedQuery = QueryHelpers.QueryUtil.addLogicFromOperator(logicalOperator, queryList=queryList)
    return completedQuery



