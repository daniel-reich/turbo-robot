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
  print(hand)
  k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  d = {'A': 0, 'K': 13, 'Q': 12, 'J': 11}
​
  suits = [card[-1] for card in hand]
  values = [card[:-1] for card in hand]
  values_ = [d[card] if card in 'KQJA' else int(card) for card in values]
  count = sum(map(values.count, values))
  
  full = count == 13
  four = count == 17
  three = count == 11
  two = count == 9
  one = count == 7
  flush = suits.count(suits[0]) == 5
  
  a = k.index(min(values_))
  b = k.index(max(values_))
  straight = b - a == 4
  print(values_)
  print(straight, b, a)
  r = [0, 11, 10, 12, 13]
  royal = [x in r for x in values_]
  r2 = [10, 11, 12, 13, 0]
  st2 = True
  for x in values_:
    if x not in r2:
      st2 = False
      break
      
  
  if flush:
    if all(royal):
      return 'Royal Flush'
    elif straight:
      return 'Straight Flush'
    else:
      return 'Flush'
  if four: return 'Four of a Kind'
  
  if full: return 'Full House'
​
  if straight or st2: return 'Straight'
​
  if three: return 'Three of a Kind'
​
  if two: return 'Two Pair'
​
  if one: return 'Pair'
​
  return 'High Card'

