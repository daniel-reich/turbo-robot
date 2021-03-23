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

import re
def poker_hand_ranking(deck):
  if is_royal_flush(deck):
    return "Royal Flush"
  if is_straight_flush(deck):
    return "Straight Flush"
  if is_four_kind(deck):
    return "Four of a Kind"
  if is_full_house(deck):
    return "Full House"
  if is_flush(deck):
    return "Flush"
  if is_straight(deck):
    return "Straight"
  if is_three_kind(deck):
    return "Three of a Kind"
  if is_two_pair(deck):
    return "Two Pair"
  if is_pair(deck):
    return "Pair"
  return "High Card"
​
def is_royal_flush(deck):
  return is_straight_flush(deck) and highest_card(deck) == "Ace"
​
def is_straight_flush(deck):
  return is_flush(deck) and is_straight(deck)
​
def is_four_kind(deck):
  return mode(deck) == 4
  
def is_full_house(deck):
  d = deck_to_list(deck)
  return mode(deck) == 3 and d.count(2) == 1
​
def is_flush(deck):
  return mode_suit(deck) == 5
  
def is_straight(deck):
  l = deck_to_list(deck)
  cntOnes = 0
  onStreak = False
  for i in l:
    if i == 1:
      if onStreak:
        cntOnes+=1
      else:
        onStreak = True
        cntOnes = 1
    else:
      onStreak = False
​
  return cntOnes == 5
      
def is_three_kind(deck):
  return mode(deck) == 3
​
def is_two_pair(deck):
  d = deck_to_list(deck)
  return mode(deck) == 2 and d.count(2) == 2
​
def is_pair(deck):
  return mode(deck) == 2
  
def mode(deck):
  return max(deck_to_list(deck))
​
def mode_suit(deck):
  return max(deck_to_suit_list(deck))
​
def card_to_index(card):
  patterns = ["2[hcsd]","3[hcsd]","4[hcds]","5[hcds]","6[hcds]","7[hcds]","8[hcds]", "9[hcds]","10[hcds]", "J[hcds]", "Q[hcds]", "K[hcds]", "A[hcds]"]
  for i, p in enumerate(patterns):
    if re.compile(p).match(card):
      return i
  return 0
​
def card_to_suit_index(card):
  patterns = [".*h",".*c",".*s",".*d"]
  for i, p in enumerate(patterns):
    if re.compile(p).match(card):
      return i
  return 0
​
def deck_to_list(deck):
  l = [0] * 13
  for card in deck:
    l[card_to_index(card)] += 1
  return l
  
def deck_to_suit_list(deck):
  l = [0] * 4
  for card in deck:
    l[card_to_suit_index(card)] += 1
  return l
​
def highest_card(deck):
  d = deck_to_list(deck)
  for i in range(len(d) - 1, -1, -1):
    if d[i] > 0:
      return index_to_card(i)
  return "Two"
  
def index_to_card(index):
  if index==12:
    return "Ace"
  return "Doesn't matter"

