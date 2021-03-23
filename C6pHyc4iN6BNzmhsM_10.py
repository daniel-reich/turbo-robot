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
  face = dict(zip('JKQA', range(11, 15)))
  vals = sorted(map(int, [face.get(x[0], x[:-1]) for x in deck]))
  straight = vals == list(range(min(vals), max(vals)+1)) 
  pairings = sorted(vals.count(x) for x in set(vals))
  
  if 4 in pairings:
    return "Four of a Kind"
  if pairings == [2, 3]:
    return "Full House"
  if 3 in pairings:
    return "Three of a Kind"
  if pairings == [1, 2, 2]:
    return "Two Pair"
  if 2 in pairings:
    return "Pair"
  
  if len(set(x[-1] for x in deck)) == 1:
    if straight and vals[0] == 10:
      return "Royal Flush"
    if straight:
      return "Straight Flush"
    return "Flush"
  
  if straight:
    return "Straight"
  
  return "High Card"

