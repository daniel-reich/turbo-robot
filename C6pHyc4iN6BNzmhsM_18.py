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

def get_rank(card):
  rank = card[:-1]
  if rank == 'J':
    return 11
  elif rank == 'Q':
    return 12
  elif rank == 'K':
    return 13
  elif rank == 'A':
    return 14
  else:
    return int(rank)
​
def get_ranks(deck):
    ranks = []
    for card in deck:
        rank = get_rank(card)
        if rank not in ranks:
            ranks.append(rank)
    ranks.sort()
    return ranks
def get_suits(deck):
    suits = []
    for card in deck:
        suit = card[-1]
        if suit not in suits:
            suits.append(suit)
    suits.sort()
    return suits
    
def count_rank(deck, rank):
    c = 0
    for card in deck:
        if get_rank(card) == rank:
            c += 1
    return c
​
def poker_hand_ranking(deck):
    ranks = get_ranks(deck)
    suits = get_suits(deck)
    
    is_straight = len(ranks) == len(deck) and ranks[-1] - ranks[0] + 1 == len(ranks)
    is_suit = len(suits) == 1
​
    #check royal flush
    if is_suit and is_straight:
        if ranks[-1] == 14:
            return 'Royal Flush'
        else:
            return 'Straight Flush'
            
    if len(ranks) == 2:
        if count_rank(deck, ranks[0]) == 4 or count_rank(deck, ranks[1]) == 4:
            return 'Four of a Kind'
        return 'Full House'
    if is_suit:
        return 'Flush'
    if is_straight:
        return 'Straight'
        
    if len(ranks) == 3:
        for rank in ranks:
            if count_rank(deck, rank) == 3:
                return 'Three of a Kind'
        return 'Two Pair'
        pair_count = 0
        for rank in ranks:
            if count(deck, rank) == 2:
                pair_count += 1
        if pair_count == 2:
            return 'Two Pair'
        
    if len(ranks) == 4:
        return 'Pair'
    
    return 'High Card'

