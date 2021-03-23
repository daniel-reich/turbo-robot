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

def get_n(hand):
  return list(map(lambda x: x[:-1], hand))
​
def royal(hand):
  return flush(hand) and ['10','A','J','K','Q'] == sorted(get_n(hand))
​
def s_f(hand):
  return st(hand) and flush(hand)
​
def flush(hand):
  return all(hand[i][-1] == hand[i-1][-1] for i in range(5))
​
def st(hand):
  order = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
  hand = sorted(get_n(hand), key=lambda x: order.index(x))
  if ["10","J","Q","K","A"] == hand: return True
  return all(order.index(hand[0])+i == order.index(hand[i]) for i in range(4))
​
def n_kind(hand, n):
  return any(get_n(hand).count(get_n(hand)[x]) == n for x in range(4))
​
def f_h(hand):
  return n_kind(hand, 2) and n_kind(hand, 3)
​
def two_p(hand):
  d = {get_n(hand)[i]: get_n(hand).count(get_n(hand)[i]) for i in range(5)} 
  return list(d.values()).count(2) == 2
  
def poker_hand_ranking(h):
  l = [royal(h),s_f(h),n_kind(h,4),f_h(h),flush(h),st(h),n_kind(h,3),two_p(h),n_kind(h,2),True]
  returns = ["Royal Flush", "Straight Flush", "Four of a Kind", "Full House",\
  "Flush", "Straight", "Three of a Kind", "Two Pair", "Pair", "High Card"]
  return [returns[x] for x in range(len(l)) if l[x] == True][0]

