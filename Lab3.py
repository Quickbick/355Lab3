# CptS 355 - Fall 2022 - Lab 3
# Nathanael Ostheller

from calendar import month
from queue import Empty


debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1 getNumCases
def getNumCases(data, counties, months):
     casesSum = 0
     for county in counties:
          if (data[county]):
               for month in months:
                    if((data[county])[month]):
                         casesSum = casesSum + (data[county])[month]
     return casesSum

## problem 2 getMonthlyCases
def getMonthlyCases(data):
     monthlyDict = {}
     for county,log in data.items():
          for month,count in log.items():
               if month not in monthlyDict.keys():
                    monthlyDict[month] = {}
               monthlyDict[month][county] = count
     return monthlyDict

from functools import reduce
## problem 3 mostCases 
def mostCases(data):
     monData = getMonthlyCases(data)
     sumValues = lambda month: reduce(lambda a, b: a+b, month.values())
     restructure = lambda t: (t[0], sumValues(t[1]))
     sums = list(map(restructure, monData.items()))
     return reduce(lambda x, y : x if x[1] > y[1] else y, sums)

## problem 4a) searchDicts(L,k)
def searchDicts(L,k):
     result = None
     for item in L:
          if(k in item.keys()):
               result = item[k]
     return result

## problem 4b) searchDicts2(L,k)
def searchDicts2h(L, k, ind):
     item = L[ind]
     if(k in item[1]):
          return item[1][k]
     elif (ind == 0):
          return None
     else:
          return searchDicts2h(L, k, item[0])

def searchDicts2(L,k):
     return searchDicts2h(L, k, len(L) - 1)

## problem 5 - getLongest

## problem 6 - apply2nextN 