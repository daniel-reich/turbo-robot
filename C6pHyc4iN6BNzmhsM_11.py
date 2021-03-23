"""


In this challenge, you have to establish which kind of Poker combination is
present in a deck of five cards. Every card is a string containing the card
value (with the upper-case initial for face-cards) and the lower-case initial
for suits, as in the examples below:

    "Ah" ➞ Ace of hearts
    "Ks" ➞ King of spades
    "3d" ➞ Three of diamonds
    "Qc" ➞ Queen of clubs

There are 10 different combinations. Here's the list, in decreasing order of
importance:

Name| Description  
---|---  
 **Royal Flush**|  A, K, Q, J, 10, all with the same suit.  
 **Straight Flush**|  Five cards in sequence, all with the same suit.  
 **Four of a Kind**|  Four cards of the same rank.  
 **Full House**|  Three of a Kind with a Pair.  
 **Flush**|  Any five cards of the same suit, not in sequence.  
 **Straight**|  Five cards in a sequence, but not of the same suit.  
 **Three of a Kind**|  Three cards of the same rank.  
 **Two Pair**|  Two different Pair.  
 **Pair**|  Two cards of the same rank.  
 **High Card**|  No other valid combination.  
  
Given a list `hand` containing five strings being the cards, implement a
function that returns a string with the name of the highest combination
obtained, accordingly to the table above.

### Examples

    poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) ➞ "Royal Flush"
    
    poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) ➞ "High Card"
    
    poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) ➞ "Four of a Kind"

### Notes

N/A

"""

cdValsA = ['2', '3', '4', '5', '6', '7', '8',
            '9', '10', 'J', 'Q', 'K', 'A']
cdValsB = ['A', '2', '3', '4', '5', '6', '7', '8',
            '9', '10', 'J', 'Q', 'K']
cdRankA = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
cdRankB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
​
dcts = [{k:v for(k,v) in zip(cdValsA, cdRankA)},
        {k:v for(k,v) in zip(cdValsB, cdRankB)}]
​
suites = ['h', 'd', 'c', 's']
​
​
#-----------------------------------------------------------------------
# Selection sort
def sortCards(dct, l):
    # ls = list of cards in hand ('10h', 'jq', etc.)
    ls = l[:]
    for i in range(0, len(ls) - 1):
        min = i
        for j in range(i + 1, len(ls)):
​
            # ls[index][0:-1] is key in dictionary
            # dct[key] is rank of card (1, 2, 3...)
            vj = dct[ls[j][0:-1]]
            vmin = dct[ls[min][0:-1]]
            if(vj < vmin):
                min = j
        if(min != i):
            tmp = ls[i]
            ls[i] = ls[min]
            ls[min] = tmp
    return(ls)
​
#-----------------------------------------------------------------------
# Verify cards in same suite
def verifySameSuite(lst):    
    # lst = list of cards in hand ('10h', 'jq', etc.)
    # s is the suite ('d', 'h', 'c', 's')
    s = lst[0][-1]
    for a in lst:
        if(a[-1] != s):
            return False
    return True
​
#-----------------------------------------------------------------------
# Verify order of cards in a hand
def verifyOrder(dct, lst):
    # lst = Sorted list of cards in hand ('10h', 'jq', etc.)
    for i in range(1, len(lst)):
        # lst[index][0:-1] is key in dictionary
        # dct[key] is rank of card (1, 2, 3...)
        if(dct[lst[i - 1][0:-1]] + 1 != dct[lst[i][0:-1]]):
            return False
    return True
​
#-----------------------------------------------------------------------
# Count pairs
def countTwos(lst):
    cnt = 0
    # lst is a list of count of cards by rank
    for i in range(len(lst)):
        if(lst[i] == 2):
            cnt += 1
    return cnt
            
#-----------------------------------------------------------------------
# Check for Royal Flush (10, J, Q, K, A or 9, 10, J, Q, K)
# Same suite
def ckRoyalFlush(sortedCrds):
    # sortedCrds is a list of 2 lists of cards sorted by rank
    # toMatch is the rank of the 1st card (10 for ace high, 9 for ace low)
    toMatch = ['10', '9']
    for i in range(2):
        # If cards are same suite
        if(verifySameSuite(sortedCrds[i])):
            # If cards all in ascending order
            if verifyOrder(dcts[i], sortedCrds[i]):
                # If 1st card the correct card for ace high/lo, return true
                if(sortedCrds[i][0][0:-1] == toMatch[i]):
                    return True
    return False
       
#-----------------------------------------------------------------------
# Check for Straight Flush - ascending order, same suite
def ckStaightFlush(sortedCrds):
    # sortedCrds is a list of 2 lists of cards sorted by rank
    for i in range(2):
        # If cards are same suite
        if(verifySameSuite(sortedCrds[i])):
            # If cards all in ascending order
            if verifyOrder(dcts[i], sortedCrds[i]):
                return True
    return False
       
#-----------------------------------------------------------------------
# Check for 4 of a kind - (4 2's, 3's, etc.)
def ckFourKind(sortedCrds):
    # sortedCrds is a SINGLE list of of cards sorted by rank
    # cnts is a list of card count by ranking
    cnts = [0] * len(dcts[0])
    # dcts[0] is 1st dictionary of card rankings
    # sortedCrds[i][0:-1]] is the key for this dictionary
    for i in range(5):
        # minus 2 keeps index in range of cnts list
        cnts[dcts[0][sortedCrds[i][0:-1]] - 2] += 1
    if(4 in cnts):
        return True
    return False
       
#-----------------------------------------------------------------------
# Check full house (i.e. '2d','2c', '3d', '3c', '3h')
def ckFullHouse(sortedCrds):
    # sortedCrds is a SINGLE list of of cards sorted by rank
    # cnts is a list of card count by ranking
    cnts = [0] * len(dcts[0])
    # dcts[0] is 1st dictionary of card rankings
    # sortedCrds[i][0:-1]] is the key for this dictionary
    for i in range(5):
        # minus 2 keeps index in range of cnts list
        cnts[dcts[0][sortedCrds[i][0:-1]] - 2] += 1
    if((3 in cnts) and (2 in cnts)):
        return True
    return False
              
#-----------------------------------------------------------------------
# Check for Flush - all cards in same suite
def ckFlush(sortedCrds):
    # sortedCrds is a SINGLE list of of cards sorted by rank
    if(verifySameSuite(sortedCrds)):
        return True
    return False
       
#-----------------------------------------------------------------------
# Check for Straight - all cards in sequential order
def ckStraight(sortedCrds):
    # sortedCrds is a list of 2 lists of cards sorted by rank
    for i in range(2):
        if verifyOrder(dcts[i], sortedCrds[i]):
            return True
    return False
       
#-----------------------------------------------------------------------
# Check for 4 of a kind - (4 2's, 3's, etc.)
def ckThreeKind(sortedCrds):
    # sortedCrds is a SINGLE list of of cards sorted by rank
    # cnts is a list of card count by ranking
    cnts = [0] * len(dcts[0])
    # dcts[0] is 1st dictionary of card rankings
    # sortedCrds[i][0:-1]] is the key for this dictionary
    for i in range(5):
        # minus 2 keeps index in range of cnts list
        cnts[dcts[0][sortedCrds[i][0:-1]] - 2] += 1
    if(3 in cnts):
        return True
    return False
       
#-----------------------------------------------------------------------
# Check for 2 pairs - (2 2's, 3's, etc., 2 2's, 3's, etc)
def ckTwoPair(sortedCrds):
    # sortedCrds is a SINGLE list of of cards sorted by rank
    # cnts is a list of card count by ranking
    cnts = [0] * len(dcts[0])
    # dcts[0] is 1st dictionary of card rankings
    # sortedCrds[i][0:-1]] is the key for this dictionary
    for i in range(5):
        # minus 2 keeps index in range of cnts list
        cnts[dcts[0][sortedCrds[i][0:-1]] - 2] += 1
    if(countTwos(cnts) == 2):
        return True
    return False
       
#-----------------------------------------------------------------------
# Check for pair - (2 2's, 3's, etc.)
def ckOnePair(sortedCrds):
    cnts = [0] * len(dcts[0])
    # dcts[0] is 1st dictionary of card rankings
    # sortedCrds[i][0:-1]] is the key for this dictionary
    for i in range(5):
        cnts[dcts[0][sortedCrds[i][0:-1]] - 2] += 1
    if(countTwos(cnts) == 1):
        return True
    return False
​
def poker_hand_ranking(hand):
    sortedCrdLst = []
    sortedCrdLst.append(sortCards(dcts[0], hand))
    sortedCrdLst.append(sortCards(dcts[1], hand))
​
    if(ckRoyalFlush(sortedCrdLst)):
        return "Royal Flush"
    elif(ckStaightFlush(sortedCrdLst)):
        return "Straight Flush"
    elif(ckFourKind(sortedCrdLst[0])):
        return "Four of a Kind"
    elif(ckFullHouse(sortedCrdLst[0])):
        return "Full House"
    elif(ckFlush(sortedCrdLst[0])):
        return "Flush"
    elif(ckStraight(sortedCrdLst)):
        return "Straight"
    elif(ckThreeKind(sortedCrdLst[0])):
        return "Three of a Kind"
    elif(ckTwoPair(sortedCrdLst[0])):
        return "Two Pair"
    elif(ckOnePair(sortedCrdLst[0])):
        return "Pair"
    else:
        return "High Card"

