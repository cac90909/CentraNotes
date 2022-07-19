#Utilizes the Query.Helper python files to make it easier to construct Mongo DB Query Objects
import Helper.QueryUtil


#comparisonOperator options include (strings): =, !=, >, >=, <, <=, e (exists), !e (does not exist), in (inside of), !in, all (match all)
def buildOneComparisonOneFieldQuery(field, comparisonOperator, value=None, valuesList=None):
    baseQuery = Helper.QueryUtil.getBaseQueryFromOperator(comparisonOperator, value, valuesList)
    completedQuery = Helper.QueryUtil.addFieldToQuery(field, baseQuery)
    return completedQuery

def buildTwoComparisonsOneFieldQuery(field, comparisonOperator1, comparisonOperator2, value1=None, valuesList1=None, value2=None, valuesList2=None):
    baseQuery1 = Helper.QueryUtil.getBaseQueryFromOperator(comparisonOperator1, value1, valuesList1)
    baseQuery2 = Helper.QueryUtil.getBaseQueryFromOperator(comparisonOperator2, value2, valuesList2)
    queryList = [baseQuery1, baseQuery2]
    combinedQuery = Helper.QueryUtil.combineQueries(queryList)
    completedQuery = Helper.QueryUtil.addFieldToQuery(field, combinedQuery)
    return completedQuery
    
#logicalOperator options include: and, or, nor
def buildTwoComparisonsTwoFieldQueryWithLogic(field1, field2, comparisonOperator1, comparisonOperator2, logicalOperator, value1=None, valuesList1=None, value2=None, valuesList2=None):
    baseQuery1 = Helper.QueryUtil.getBaseQueryFromOperator(comparisonOperator1, value1, valuesList1)
    baseQuery2 = Helper.QueryUtil.getBaseQueryFromOperator(comparisonOperator2, value2, valuesList2)
    baseQueryWithField1 = Helper.QueryUtil.addFieldToQuery(field1, baseQuery1)
    baseQueryWithField2 = Helper.QueryUtil.addFieldToQuery(field2, baseQuery2)
    queryList = [baseQueryWithField1, baseQueryWithField2]
    completedQuery = Helper.QueryUtil.addLogicFromOperator(logicalOperator, queryList=queryList)
    return completedQuery



