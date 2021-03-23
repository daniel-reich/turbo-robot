"""


In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

 **S.No.**|  **Hand Rank**|  **Explanation**  
---|---|---  
1|  **High Card**|  Highest value card.  
2|  **One Pair**|  Two cards of the same value.  
3|  **Two Pairs**|  Two different pairs.  
4|  **Three of a Kind**|  Three cards of the same value.  
5|  **Straight**|  All cards are consecutive values.  
6|  **Flush**|  All cards of the same suit.  
7|  **Full House**|  Three of a kind and a pair.  
8|  **Four of a Kind**|  Four cards of the same value.  
9|  **Straight Flush**|  All cards are consecutive values of same suit.  
10|  **Royal Flush**|  Ten, Jack, Queen, King, Ace, in same suit.  
  
The cards are valued in the order:

    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace

If two players have the same ranked hands then the rank made up of the highest
value wins. For example, a pair of eights beats a pair of fives (see example
#1). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example #4). If the highest
cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

 **Hand**|  **Player 1**|  **Player 2**|  **Winner**  
---|---|---|---  
1| 5H 5C 6S 7S KD| 2C 3S 8S 8D TD| Player 2  
2| 5D 8C 9S JS AC| 2C 5C 7D 8S QH| Player 1  
3| 2D 9C AS AH AC| 3D 6D 7D TD QD| Player 2  
4| 4D 6S 9H QH QC| 3D 6D 7H QD QS| Player 1  
5| 2H 2D 4C 4D 4S| 3C 3D 3S 9S 9D| Player 1  
  
Create a function which takes list of random hands dealt to two players. Each
string contains ten cards (separated by a single space). The first five are
Player 1's cards and the last five are Player 2's cards. The function should
return the number of hands Player 1 won.

### Examples

    player1_wins([
      "8C TS KC 9H 4S 7D 2S 5D 3S AC",
      "5C AD 5D AC 9C 7C 5H 8D TD KS",
      "3H 7H 6S KC JS QH TD JC 2D 8S",
      "TH 8H 5C QS TC 9H 4D JC KS JS",
      "7C 5H KC QH JD AS KH 4C AD 4S"
    ]) ➞ 2
    
    player1_wins([
      "5H QS 8S 6D 3C 8C JD AS 7H 7D",
      "6H TD 9D AS JH 6C QC 9S KD JC",
      "AH 8S QS 4D TH AC TS 3C 3D 5C",
      "5S 4D JS 3D 8H 6C TS 3S AD 8C",
      "6D 7C 5D 5H 3S 5C JC 2H 5S 3D",
      "5H 6H 2S KS 3D 5D JD 7H JS 8H",
      "KH 4H AS JS QS QC TC 6D 7C KS",
      "3D QS TS 2H JS 4D AS 9S JC KD",
      "QD 5H 4D 5D KH 7H 3D JS KD 4H"
    ]) ➞ 3
    
    player1_wins([
      "5S 9C KH KD 9H 5C TS 3D 7D 2D",
      "5H AS TC 4D 8C 2C TS 9D 3H 8D"
    ]) ➞ 2

### Notes

  * Assume all hands are valid (no invalid characters or repeated cards).
  * Each player's hand is in no specific order.
  * In each hand there is a clear winner.
  * Ten is given as **T** instead of 10.

"""

def player1_wins(lst):
    '''
    Returns a count of the number of times player1 wins for each pair of hands
    in lst, as per the rules of poker outlined in the instructions
    '''
    from collections import Counter
​
    RANKS = ('AKQJT98765432')
    VALUES = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    
    value = lambda x: VALUES[x[0]] if x[0] in VALUES else int(x[0]) # single card
​
    is_flush = lambda x: all(x[i][1] == x[0][1] for i in range(1,5))
​
    is_straight = lambda x: all(value(x[i][0]) == value(x[i-1][0]) - 1
                                for i in range(1,5)) 
    
    highest = lambda x,y=None: value(x[0])
​
    straight_flush = lambda x,y: 180 + value(x[0]) if (is_straight(x) and is_flush(x))\
                     else 0  # automatically scores royal flush higher
​
    four_kind = lambda x,y: 160 + value(y[0][1]) if y[0][0] == 4 else 0
​
    full_house = lambda x,y: 140 + value(y[0][1]) if (y[0][0] == 3 and y[0][1] == 2) \
                 else 0
                 
    three_kind = lambda x,y: 80 + value(y[0][1]) if y[0][0] == 3 else 0
​
    two_pairs = lambda x,y: 60 + value(y[0][1]) if (y[0][0] == 2 and y[0][1] == 2) \
                 else 0
​
    one_pair = lambda x,y: 40 + value(y[0][1]) if y[0][0] == 2 else 0
​
    straight = lambda x,y: 100 if is_straight(x) else 0
​
    flush = lambda x,y: 120 if is_flush(x) else 0
​
    hand_checks = (straight_flush, four_kind, flush, straight,
                   three_kind, two_pairs, one_pair, highest) # check in this order
    scores = [0,0]  # score each hand
​
    count = 0
    for hands in lst:
        hands = hands.split()
        p1 = sorted([hands[i] for i in range(5)],
                         key=lambda x: RANKS.index(x[0]))
        p2 = sorted([hands[i] for i in range(5,10)],
                         key=lambda x: RANKS.index(x[0]))
        dealt = (p1, p2)
        values = []
        
        for i in range(len(scores)):
            ranks = ''.join(c[0] for c in dealt[i])
            values.append(sorted(set([(ranks.count(s),s) for s in ranks]), reverse=True))  # for use in n of a kind checks
            
            for check in hand_checks:
                score = check(dealt[i], values[i])
                if score:
                    scores[i] = score
                    break
​
        if scores[0] > scores[1]: # p1 won
            count += 1
        elif scores[0] == scores[1]:  # same - need highest
            for i in range(len(values[0])):
                p1v, p2v = value(values[0][i][1]), value(values[1][i][1])
                if p1v == p2v:
                    continue
                if p1v > p2v:  # p1 wins tie-breaker
                    count += 1
                break
​
    return count

