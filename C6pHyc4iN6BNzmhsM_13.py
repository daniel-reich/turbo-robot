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
    rank_translation = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    tpl_lst = sorted([(rank_translation[card[:-1]]
                       if card[:-1] in rank_translation else int(card[:-1]),
                       card[-1]) for card in deck])
    ranks = list(card[0] for card in tpl_lst)
    suits = list(card[1] for card in tpl_lst)
    ranks_count = sorted([ranks.count(rank) for rank in set(ranks)])
    if len(set(suits)) == 1 and ranks == [10, 11, 12, 13, 14]:
        return 'Royal Flush'
    if len(set([tpl_lst[i][0] - tpl_lst[i - 1][0]
                for i in range(1, len(tpl_lst))])) == 1:
        if len(set(suits)) == 1:
            return 'Straight Flush'
        else:
            return 'Straight'
    if len(set(suits)) == 1:
        return 'Flush'
    if 4 in ranks_count:
        return 'Four of a Kind'
    if ranks_count == [2, 3]:
        return 'Full House'
    if 3 in ranks_count:
        return 'Three of a Kind'
    if ranks_count.count(2) == 2:
        return 'Two Pair'
    if 2 in ranks_count:
        return 'Pair'
    return 'High Card'

