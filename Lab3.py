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

## problem 4a) searchDicts(L,k)
## problem 4b) searchDicts2(L,k)

## problem 5 - getLongest

## problem 6 - apply2nextN 