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

import collections
​
Card = collections.namedtuple("Card", "num suit")
d = {'2': 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}
​
def poker_hand_ranking(deck):
    deck = [Card(item[:-1], item[-1]) for item in deck]
    suit_counter = collections.Counter([card.suit for card in deck])
    num_counter = collections.Counter([card.num for card in deck])
    nums = [d[card.num] for card in deck]
    print(sorted(nums))
    if flush(suit_counter) and royal(nums):
        return "Royal Flush"
    elif flush(suit_counter) and straight(nums):
        return "Straight Flush"
    elif four_of_a_kind(num_counter):
        return "Four of a Kind"
    elif full_house(num_counter):
        return "Full House"
    elif flush(suit_counter):
        return "Flush"
    elif straight(nums):
        return "Straight"
    elif three_of_a_kind(num_counter):
        return "Three of a Kind"
    elif two_pair(num_counter):
        return "Two Pair"
    elif two_of_a_kind(num_counter):
        return "Pair"
    else:
        return "High Card"
        
def flush(suit_counter):
    return 5 in suit_counter.values()
​
def four_of_a_kind(num_counter):
    return 4 in num_counter.values()
​
def full_house(suit_counter):
    return sorted(suit_counter.values()) == [2, 3]
​
def three_of_a_kind(num_counter):
    return 3 in num_counter.values()
​
def two_pair(num_counter):
    return sorted(num_counter.values()) == [1, 2, 2]
​
def two_of_a_kind(num_counter):
    return sorted(num_counter.values()) == [1, 1, 1, 2]
​
def royal(nums):
    return sorted(nums) == [10, 11, 12, 13, 14]
​
def straight(nums):
    order = [i for i in range(2, 15)]
    return sorted(nums) in [order[n:n+5] for n in range(9)]

