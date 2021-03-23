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
    hl, sl, dl, cl, e = [], [], [], [], []
    total = [hl, sl, dl, cl]
    for x in range(len(hand)): hand[x] = hand[x].replace("A", "14").replace("K", "13").replace("Q", "12").replace("J", "11")
    flush,toak,pair = False,False,False
    for a in hand:
        e.append(int(a[:-1]))
        if a[-1] == "h": hl.append(int(a[:-1]))
        elif a[-1] == "s": sl.append(int(a[:-1]))
        elif a[-1] == "d": dl.append(int(a[:-1]))
        elif a[-1] == "c": cl.append(int(a[:-1]))
    for l in total:
        l.sort()
        if len(l) == 5:
            if l[0] == 10 and l[4] == 14: return "Royal Flush"
            if l == list(range(l[0],l[4]+1)): return "Straight Flush"
            flush = True
    for x in e:
        if e.count(x) == 4: return "Four of a Kind"
    for x in e:
        if e.count(x) == 3: toak = True
    for x in e:
        if e.count(x) == 2: pair = True
    if toak and pair: return "Full House"
    if flush: return "Flush"
    e.sort()
    if e == list(range(e[0],e[4]+1)): return "Straight"
    if toak: return "Three of a Kind"
    if pair:
        pair = False
        for x in e:
            if e.count(x) == 2:
                if pair: return "Two Pair"
                pair = True
                e.remove(x)
    if pair: return "Pair"
    return "High Card"

