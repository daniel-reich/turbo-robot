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

card_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
​
def hand_rank(hand):
    a = sorted([i[0] for i in hand])
    
    #Royal Flush
    if a == sorted(["A", "K", "Q", "J", "T"]) and len(set(i[1] for i in hand)) == 1:
        return (10, )
    
    #Straight Flush
    elif a == sorted(card_ranks[card_ranks.index(a[0]):card_ranks.index(a[0]) + 5]) and len(set(i[1] for i in hand)) == 1:
        return (9, )
    elif len(set(a)) == 2:
        
        #Four of a Kind
        if 4 in [a.count(i) for i in a]:
            return (8, card_ranks.index([i for i in a if a.count(i) == 4][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 4], reverse = True))
        
        #Full House
        else:
            return (7, card_ranks.index([i for i in a if a.count(i) == 3][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 3], reverse = True))
    
    #Flush
    elif len(set(i[1] for i in hand)) == 1:
        return (6, )
    
    #Straight
    elif a == sorted(card_ranks[card_ranks.index(a[0]):card_ranks.index(a[0]) + 5]):
        return (5, )
    elif len(set(a)) == 3:
        
        #Three of a Kind
        if sorted([a.count(i) for i in a]) == [1, 1, 3, 3, 3]:
            return (4, card_ranks.index([i for i in a if a.count(i) == 3][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 3], reverse = True))
        
        #Two Pairs
        else:
            return (3, card_ranks.index([i for i in a if a.count(i) == 2][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 2], reverse = True))
    
    #One Pair
    elif sorted([a.count(i) for i in a]) == [1, 1, 1, 2, 2]:
        return (2, card_ranks.index([i for i in a if a.count(i) == 2][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 2], reverse = True))
    
    #High Card
    else:
        b = sorted([card_ranks.index(i) for i in a], reverse = True)
        b.remove(max(card_ranks.index(i) for i in a))
        return (1, max(card_ranks.index(i) for i in a), b)
​
​
def winner(pl1, pl2):
    if hand_rank(pl1)[0] > hand_rank(pl2)[0]:
        return "Player1"
    elif hand_rank(pl1)[0] < hand_rank(pl2)[0]:
        return "Player2"
    else:
        if hand_rank(pl1)[1] > hand_rank(pl2)[1]:
            return "Player1"
        elif hand_rank(pl1)[1] < hand_rank(pl2)[1]:
            return "Player2"
        else:
            for i in range(5):
                if hand_rank(pl1)[2][i] > hand_rank(pl2)[2][i]:
                    return "Player1"
                elif hand_rank(pl1)[2][i] < hand_rank(pl2)[2][i]:
                    return "Player2"
                else:
                    continue
​
def player1_wins(lst):
    c = 0
    for i in lst:
        p1 = i.split(" ")[:5]
        p2 = i.split(" ")[5:]
        if winner(p1, p2) == "Player1":
            c += 1
    return c

