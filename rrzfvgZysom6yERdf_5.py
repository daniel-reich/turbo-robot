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
    ]) ??? 2
    
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
    ]) ??? 3
    
    player1_wins([
      "5S 9C KH KD 9H 5C TS 3D 7D 2D",
      "5H AS TC 4D 8C 2C TS 9D 3H 8D"
    ]) ??? 2

### Notes

  * Assume all hands are valid (no invalid characters or repeated cards).
  * Each player's hand is in no specific order.
  * In each hand there is a clear winner.
  * Ten is given as **T** instead of 10.

"""

def check_playerone(lst):
    a = []
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    maxes = [sorted([values.index(y[0]) for y in x]) for x in lst]
    d = {}
    for i, player in enumerate(lst):
        suits = [x[1] for x in player]
        faces = [x[0] for x in player]
        straight = any(not set(values[x:x+5]).difference(faces)for x in range(9))
        flush = len(set(suits)) == 1
        pairs = [x for x in faces if faces.count(x) == 2]
???
        if flush and not set(faces).difference(values[8:13]):
            a.append(10)
        
        elif flush and straight:
            a.append(9)
        
        elif faces.count(max(faces, key=faces.count)) == 4:
            a.append(8)
        
        elif faces.count(max(faces, key=faces.count)) == 3 and pairs:
            a.append(7)
        
        elif flush:
            a.append(6)
        
        elif straight:
            a.append(5)
        
        elif faces.count(max(faces, key=faces.count)) == 3:
            a.append(4)
        
        elif len(pairs) == 4:
            a.append(3)
        
        elif len(pairs) == 2:
            d[i] = pairs[0]
            a.append(2)
        else:
            a.append(False)
???
    # print(lst, a)
    if not a[0] and not a[1]:
        if max(maxes, key=sum) == maxes[0]:
            return True
        else:
            return False
    if a[0] == a[1]:
        if max(d[0], d[1], key=values.index) == d[0]:
            return True
    if not a[0]:
        return False
    if max(a) == a[1]:
        return False
???
    return True
???
def player1_wins(lst):
    lst = [[x.split()[:5], x.split()[5:]] for x in lst]
    p1 = 0
    
    for x in lst:
        if check_playerone(x):
            p1 += 1
???
    return p1

