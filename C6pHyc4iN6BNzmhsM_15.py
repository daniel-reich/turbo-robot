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
    def compare(elem):
            return rank[elem]
    hands=["Royal Flush","Straight Flush","Four of a Kind","Full House","Flush","Straight","Three of a Kind","Two Pair","Pair","High Card"]
    rank=list("23456789")+["10"]+list("JQKA")
    rank=dict(enumerate(rank))
    rank = {y:x for x,y in rank.items()}
    suits=[elem[-1] for elem in hand]
    ranks=[elem[:-1] for elem in hand]
    ranks=sorted (ranks, key = compare)
    suit_freq = {x:suits.count(x) for x in suits}
    rank_freq = {x:ranks.count(x) for x in ranks}
    if len(rank_freq)==2 and max(rank_freq.values())==4:
        return hands[2]
    elif len(rank_freq)==2 and max(rank_freq.values())==3:
        return hands[3]
    elif len(rank_freq)==3 and max(rank_freq.values())==3:
        return hands[6]
    elif len(suit_freq)==1 and all([1 if rank in ["A","Q","K","J","10"] else 0 for rank in ranks]):
        return hands[0]
    elif len(suit_freq)==1 :                
        if all([1 if rank[ranks[index]]==rank[ranks[index+1]]-1 else 0  for index in range(4)]):
            return hands[1]
        else:
            return hands[4]
    elif all([1 if rank[ranks[index]]==rank[ranks[index+1]]-1 else 0  for index in range(4)]):
        return hands[5]
    elif  len(suit_freq)==1 :
        return hands[4]
    elif len (rank_freq)==3:
        return hands[7]
    elif len(rank_freq)==4:
        return hands[8]
    else:
        return hands[9]

