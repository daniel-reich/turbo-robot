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

from collections import defaultdict
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
class Card:
  def __init__(self, istr):
    self.string = istr.lower()
    self.face = self.string[:-1]
    self.suit = self.string[-1]
​
  def __lt__(self, other):
    return faces.index(self.face) < faces.index(other.face)
​
  def __eq__(self, other):
    return self.face == other.face and self.suit != other.suit
​
def poker_hand_ranking(hand):
  hand = sorted(Card(card) for card in hand)
  if len(set([card.suit for card in hand])) == 1:
    if [card.face for card in hand] == faces[-5:]: return "Royal Flush"
    elif [card.face for card in hand] == faces[faces.index(hand[0].face):faces.index(hand[-1].face)+1]: return "Straight Flush"
  hand_faces = defaultdict(int)
  hand_suits = defaultdict(int)
  for card in hand:
    hand_faces[card.face] += 1
    hand_suits[card.suit] += 1
  hfv, hsv = list(hand_faces.values()), list(hand_suits.values())
  if 4 in hfv: return "Four of a Kind"
  elif 3 in hfv and 2 in hfv: return "Full House"
  elif 5 in hsv: return "Flush"
  elif [card.face for card in hand] == faces[faces.index(hand[0].face):faces.index(hand[-1].face)+1]: return "Straight"
  elif 3 in hfv: return "Three of a Kind"
  elif hfv.count(2)==2: return "Two Pair"
  elif hfv.count(2)==1: return "Pair"
  return "High Card"

