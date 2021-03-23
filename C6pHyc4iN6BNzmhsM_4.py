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

def poker_hand_ranking(hand):
  #Sorted hand of cards (Value:int,Suit:str)
  myHand=[letterToNum(hand[0]),letterToNum(hand[1]),letterToNum(hand[2]),letterToNum(hand[3]),letterToNum(hand[4])]
  myHand.sort()
  
  #Check Suit
  if 5 in countSuits(myHand):
    #Check Royal Flush
    if myHand[0][0]>=10 and myHand[1][0]>=10 and myHand[2][0]>=10 and myHand[3][0]>=10 and myHand[4][0]>=10:
      return("Royal Flush")
    #Check Straight Flush
    elif checkStraight(myHand)==5: return("Straight Flush")
    else: return("Flush")
  #End Check Suit
​
  #Check Four of A Kind
  if 4 in sameRanks(myHand): return("Four of a Kind")
​
  #Check Full House
  if 2 in sameRanks(myHand) and 3 in sameRanks(myHand): return("Full House")
​
  #Check Straight
  if checkStraight(myHand)==5: return("Straight")
​
  #Check Three of A Kind
  if 3 in sameRanks(myHand): return("Three of a Kind")
​
  #Check Two Pair, Pair, High Card
  if sameRanks(myHand).count(2)==2: return("Two Pair")
  elif sameRanks(myHand).count(2)==1: return("Pair")
  else: return("High Card")
​
def letterToNum(card):
  if card[0:-1]=="A":
    return [14,card[-1]]
  elif  card[0:-1]=="K":
    return [13,card[-1]]
  elif  card[0:-1]=="Q":
    return [12,card[-1]]
  elif  card[0:-1]=="J":
    return [11,card[-1]]
  else:
    return [int(card[0:-1]),card[-1]]
    
def countSuits(handed):
  # c d h s
  suits=[0,0,0,0]
  for subList in handed:
    if subList[1]=="c": suits[0]+=1
    elif subList[1]=="d": suits[1]+=1
    elif subList[1]=="h": suits[2]+=1
    elif subList[1]=="s": suits[3]+=1
    else: pass
  return suits
  
def checkStraight(handed):
  count=1
  i = 1
  while i<5:
    if handed[i][0]==((handed[i-1][0])+1):
      count+=1
      i+=1
    else: i+=1
  return count
​
def sameRanks(handed):
  #count=0
  #2 3 4 5 6 7 8 9 10 j11 q12 k13 a14
  ranking=[0,0,0,0,0,0,0,0,0,0,0,0,0]
  i=2
  while i<15:
    j=i-2
    ranking[j]=getRanking(handed,i)
    i+=1
  
  return ranking
​
def getRanking(lst, val):
  count=0
  for subLst in lst:
    if subLst[0]==val: count+=1
    else: pass
  
  return count

