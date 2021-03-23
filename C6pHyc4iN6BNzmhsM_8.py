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
  def _value_card(card):
    if card == "A":
      return 14
    if card == "K":
      return 13
    if card == "Q":
      return 12
    if card == "J":
      return 11
    return int(card)
  
  def _is_straight(cs):
    if cs[-1] - cs[0] == 4:
      return True
    if cs[-1] == 14 and cs[0] == 2 and cs[-2] == 5:
      return True
    return False
    
  def _value_suit(suit):
    if suit == "s":
      return 0
    if suit == "h":
      return 1
    if suit == "d":
      return 2
    return 3
  
  suits = [_value_suit(x[-1]) for x in hand]
  cards = sorted([_value_card(x[:-1]) for x in hand])
  same_suit = len(set(suits)) == 1
  is_straight = _is_straight(cards)
  
  if same_suit and is_straight:
    if cards[0] == 10:
      return "Royal Flush"
    return "Straight Flush"
  
  num_cards = len(set(cards))
  
  if num_cards == 2:
    if cards[0] == cards[3] or cards[1] == cards[4]:
      return "Four of a Kind"
    return "Full House"
  
  if same_suit:
    return "Flush"
  
  if is_straight:
    return "Straight"
  
  for i in range(len(cards) - 2):
    if cards[i] == cards[i + 1] == cards[i + 2]:
      return "Three of a Kind"
  
  pairs = 0
  for i in range(len(cards) - 1):
    if cards[i] == cards[i + 1]:
      pairs += 1
  
  if pairs == 2:
    return "Two Pair"
  elif pairs == 1:
    return "Pair"
  
  return "High Card"

