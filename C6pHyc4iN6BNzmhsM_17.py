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

def consecutive_difs(lst):
  difs = []
  for i in range(1, len(lst)):
    difs.append( lst[i] - lst[i-1] )
  return difs
  
def counter(lst):
  counts = []
  for item in lst:
    counts.append(lst.count(item))
  return counts
​
def poker_hand_ranking(hand):
  ranks = []
  suits = []
  face_cards = {'A':14, 'K':13, 'Q':12, 'J':11}
  for card in hand:
    suits.append( card[-1] )
    try:
      ranks.append( int(card[:-1]) )
    except ValueError:
      ranks.append( face_cards[ card[:-1] ] )
      
  if len(set(suits)) == 1:    # have some type of flush
    if consecutive_difs( sorted(ranks) ) == [1, 1, 1, 1]:
      if max(ranks) == 14:
        return 'Royal Flush'
      else:
        return 'Straight Flush'
    else:
      return 'Flush'
      
  elif consecutive_difs( sorted(ranks) ) == [1, 1, 1, 1]:
    return 'Straight'
    
  else:
    if sorted( counter(ranks) ) == [1, 4, 4, 4, 4]:
      return 'Four of a Kind'
    elif sorted( counter(ranks) ) == [2, 2, 3, 3, 3]:
      return 'Full House'
    elif sorted( counter(ranks) ) == [1, 1, 3, 3, 3]:
      return 'Three of a Kind'
    elif sorted( counter(ranks) ) == [1, 2, 2, 2, 2]:
      return 'Two Pair'
    elif sorted( counter(ranks) ) == [1, 1, 1, 2, 2]:
      return 'Pair'
    else:
      return 'High Card'

