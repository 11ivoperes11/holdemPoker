handDict = {
    1 : ['k','♠'],
    2 : [10,'♠'],
    3 : [8,'♠'],
    4 : [7,'♠'],
    5 : [5,'♠']
}

print(handDict[1][0])           # how to access list items within dictionary

"""Generates duplicate counts of card values"""
dupValDict = {}
cardValList = ['k','k',10,7,7]    # imagine this is the list of card numbers, obtained by isolating them from handDict
for cardVal in cardValList:
    dupCount = 0
    for compare in cardValList:
        if cardVal == compare:
            dupCount = dupCount + 1
    if dupCount >= 2:
        dupValDict[cardVal] = dupCount

print(dupValDict)

"""Generates duplicate counts of suites"""
dupSuiteDict = {}
cardSuiteList = ['♠','♠','♠','♠','♠']
for suite in cardSuiteList:
    dupCount = 0
    for compare in cardSuiteList:
        if suite == compare:
            dupCount = dupCount + 1

    if dupCount >= 2:
        dupSuiteDict[suite] = dupCount

print(dupSuiteDict)

"""Checks Duplicate values"""
pairCount = 0
tripCount = 0
quadCount = 0
suiteFlush = 0
for i in dupValDict:
    dupCount = dupValDict[i]
    if dupCount == 2: 
        pairCount = pairCount + 1
    elif dupCount == 3:
        tripCount = tripCount + 1
    elif dupCount == 4:
        quadCount = quadCount + 1


    print(dupSuiteDict[i])
"""checks duplicate suites
for i in dupSuiteDict:
    if dupSuiteDict[i] == 5:
    suiteFlush = suiteFlush + 1
"""

"""checks if 5 cards are sequentially ordered
if len(dupValDict) == 5:
    for value in dupValDict:
        print(dupValDict[value])
"""




    
 