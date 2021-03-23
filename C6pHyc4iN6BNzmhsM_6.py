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

def poker_hand_ranking(deck):
  import re
  d={'J':12,'Q':13,'K':14,"A":11}
  res=[re.sub( r"([a-z])", r" \1", s).split() \
  for s in [str(d[i[0]])+ i[1] if i[0] in 'JQKA' else i for i in deck]]
  tmp = sorted([int(row[0]) for row in res])
  tmp_= sorted([int(row[0]) for row in res])
  tmp1= list(set(tmp))
  if (sorted([10,11,12,13,14]) == sorted(tmp) and len(set([row[1] \
  for row in res]))==1):
    return('Royal Flush')
  elif (len(set(sorted(tmp)))==5 and len(set([row[1] for row in res]))==1):
    if tmp[0] == tmp[1]-1 and tmp[1]==tmp[2]-1 and tmp[2]==tmp[3]-1\
    and tmp[3] == tmp[4]-1:
      return('Straight Flush')
    else:
      if not(tmp.count(list(set(tmp))[0])==4 or \
      tmp.count(list(set(tmp))[1])==4):
        return('Flush')
  elif (len(set(sorted(tmp)))<=2):
    if tmp.count(list(set(tmp))[0])==4 or \
    tmp.count(list(set(tmp))[1])==4 :
      return('Four of a Kind')
    else:
      return('Full House')
  elif (len(set(sorted(tmp)))==5 and not len(set([row[1] \
  for row in res]))==1):
    if tmp[0] == tmp[1]-1 and tmp[1]==tmp[2]-1 and tmp[2]==tmp[3]-1 and\
    tmp[3] == tmp[4]-1:
      return('Straight')
    else:
      return ("High Card")
  elif (len(set(sorted(tmp)))<=3):
    if tmp.count(tmp1[0])==3 or tmp.count(tmp1[1])==3 or  \
    tmp.count(tmp1[2])==3:
      return('Three of a Kind')
    else:
      return('Two Pair')
  elif (len(set(sorted(tmp)))==4):
    return('Pair')

