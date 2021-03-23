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

def check_flush(deck):
    if len(set([x[-1] for x in deck])) == 1:
        return True
​
​
def check_straight(deck):
    numbers = [int(x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for x in deck]
    numbers.sort()
    if (numbers[4] - numbers[0]) == 4:
        return True
    return False
​
​
def check_royal(deck):
    numbers = [int(x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for x in deck]
    if 14 in numbers:
        return True
    return False
​
​
def check_four_of_a_kind(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 4:
        return True
    return False
​
​
def check_full_house(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 3 and min(counts) == 2:
        return True
    return False
​
​
def check_three_of_a_kind(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 3:
        return True
    return False
​
​
def check_two_pair(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 2 and len(set(numbers)) == 3:
        return True
    return False
​
​
def check_pair(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 2:
        return True
    return False
​
​
def poker_hand_ranking(deck):
    if check_flush(deck):
        if check_straight(deck):
            if check_royal(deck):
                return "Royal Flush"
            else:
                return "Straight Flush"
        else:
            return "Flush"
    elif check_four_of_a_kind(deck):
        return "Four of a Kind"
​
    elif check_full_house(deck):
        return "Full House"
​
    elif check_straight(deck):
        return "Straight"
​
    elif check_three_of_a_kind(deck):
        return "Three of a Kind"
​
    elif check_two_pair(deck):
        return "Two Pair"
​
    elif check_pair(deck):
        return "Pair"
​
    else:
        return "High Card"

