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
      
  cards = [x[:-1] for x in hand]
  postupnost = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  highest_straight = (set(cards) == {"10", "J", "Q", "K", "A"})
  min_index = min([postupnost.index(x) for x in cards])
  straight = True
  
  for i in range(1,5):
      if postupnost[min_index+i] in set(cards):
          continue
      else:
          straight = False
              
  # Four of a kind
      
  four = False
      
  for card in cards:
      if cards.count(card) == 4:
          four = True
          break
  
  # Fullhouse
  fh_list = [cards.count(card) for card in cards] 
  fullhouse = (fh_list.count(3) == 3) and (fh_list.count(2) == 2)    
​
  same_color = (lambda hand: (hand[0][-1] == hand[1][-1] == hand[2][-1] == hand[3][-1] == hand[4][-1]))(hand)
  
  if same_color and highest_straight:
      return "Royal Flush"
  
  if straight == True and same_color == True:
      return "Straight Flush"
  
  if four:
      return "Four of a Kind"    
      
  if same_color:
      return "Flush"
  
  if fullhouse:
      return "Full House"
         
  if straight:
      return "Straight"
  
  three = fh_list.count(3) == 3
  if three:
      return "Three of a Kind"
  
  twopair = fh_list.count(2) == 4   
  if twopair:
      return "Two Pair"
      
  onepair = fh_list.count(2) == 2   
  if onepair:
      return "Pair"    
  
  return "High Card"

