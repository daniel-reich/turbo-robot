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
​
  class Hand:
    
    royal_flush ='T, J, Q, K, A'.split(', ')
​
    def __init__(self, hand):
      self.hand = hand
​
      self.vals = []
      self.suits = []
      self.dic = {}
​
      for item in hand:
        try:
          self.vals.append(int(item[0]))
          value = int(item[0])
        except ValueError:
          dic = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
          if item[0] in dic.keys():
            self.vals.append(dic[item[0]])
            value = item[0]
        
        self.suits.append(item[1])
        if item[1] not in self.dic.keys():
          self.dic[item[1]] = [value]
        else:
          self.dic[item[1]].append(value)
​
      self.high_crd = max(self.vals)
​
      if len(self.suits) == 1:
        if sorted(self.dic[self.suits[0]]) == sorted(Hand.royal_flush):
          self.rf = True
        else:
          self.rf = False
      else:
        self.rf = False
      
      self.pairs = 0
      self.triple = False
      self.fourth = False
​
      for item in set(self.vals):
        c = self.vals.count(item)
        if c == 2:
          self.pairs += 1
        if c == 3:
          self.triple = True
        if c == 4:
          self.fourth = True
      
      if len(list(set(self.suits))) == 1:
        self.samesuit = True
      else:
        self.samesuit = False
      
      self.consec = False
​
      difs = []
​
      for n in range(len(self.vals)-1):
        prev = self.vals[n]
        curr = self.vals[n+1]
​
        difs.append(curr-prev)
​
      difs = list(set(difs))
      
      if len(difs) == 1 and difs[0] == 1:
        self.consec = True
      
    def versus(self, other):
      highest_card = self.high_crd
      highest_rank = 1
​
      if self.rf == True:
        highest_rank = 10
      elif self.consec == True and self.samesuit == True:
        highest_rank = 9
      elif self.fourth == True:
        highest_rank = 8
      elif self.triple == True and self.pairs == 1:
        highest_rank = 7
      elif self.samesuit == True:
        highest_rank = 6
      elif self.consec == True:
        highest_rank = 5
      elif self.triple == True:
        highest_rank = 4
      elif self.pairs == 2:
        highest_rank = 3
      elif self.pairs == 1:
        highest_rank = 2
      
      o_hc = other.high_crd
      o_highest_rank = 1
​
      if other.rf == True:
        o_highest_rank = 10
      elif other.consec == True and other.samesuit == True:
        o_highest_rank = 9
      elif other.fourth == True:
        o_highest_rank = 8
      elif other.triple == True and other.pairs == 1:
        o_highest_rank = 7
      elif other.samesuit == True:
        o_highest_rank = 6
      elif other.consec == True:
        o_highest_rank = 5
      elif other.triple == True:
        o_highest_rank = 4
      elif other.pairs == 2:
        o_highest_rank = 3
      elif other.pairs == 1:
        o_highest_rank = 2
  
      if highest_rank > o_highest_rank:
        return 1
      elif highest_rank < o_highest_rank:
        return 0
      else:
        if highest_rank == 9:
          if highest_card > o_hc:
            return 1
          elif highest_card < o_hc:
            return 0
        if highest_rank == 8:
          bi = None
          for item in set(self.vals):
            if self.vals.count(item) == 4:
              bi = item
              break
          obi = None
          for item in set(other.vals):
            if other.vals.count(item) == 4:
              obi = item
              break
          if bi > obi:
            return 1
          elif bi < obi:
            return 0
        if highest_rank == 7:
          ss = list(set(self.vals))
          os = list(set(other.vals))
​
          if max(ss) == max(os):
            if min(ss) > min(os):
              return 1
            return 0
          if max(ss) > max(os):
            return 1
          else:
            return 0
        if highest_rank == 6:
          ss = sorted(self.vals)
          os = sorted(other.vals)
​
          for n in range(1, len(ss)+1):
            si = ss[-n]
            oi = os[-n]
​
            if si > oi:
              return 1
            elif s1 < oi:
              return 0
         # print(self.vals, other.vals)
          return 0
        if highest_rank == 5:
          if max(self.vals) > max(other.vals):
            return 1
          return 0
        if highest_rank == 4:
          ss = sorted(list(set(self.vals)))
          os = sorted(list(set(self.vals)))
​
          for n in range(1, len(ss)):
            si = ss[-n]
            oi = os[-n]
​
            if si > oi:
              return 1
            elif s1 < oi:
              return 0
            
          #print(self.vals, other.vals)
          return 0
        if highest_rank == 3:
          pair_vals = []
          
          for item in set(self.vals):
            c = self.vals.count(item)
            if c == 2:
              pair_vals.append(item)
          
          opv = []
​
          for item in set(other.vals):
            c = other.vals.count(item)
            if c == 2:
              opv.append(item)
          
          if max(pair_vals) > max(opv):
            return 1
          elif max(pair_vals) < max(opv):
            return 0
          else:
            if min(pair_vals) > min(pair_vals):
              return 1
            elif min(pair_vals) < min(pair_vals):
              return 0
            else:
              for item in set(self.vals):
                if item not in pair_vals:
                  remaining_item = item
                  break
              for item in set(other.vals):
                if item not in opv:
                  ori = item
                  break
              
              if remaining_item > ori:
                return 1
              elif remaining_item < ori:
                return 0
              else:
                print (self.vals, other.vals)
                return 0
​
        if highest_rank == 2:
          pairval = 0
          for item in self.vals:
            c = self.vals.count(item)
            if c == 2:
              pairval = item
          ov = 0
          for item in other.vals:
            #print(item, other.vals.count(item))
            c = other.vals.count(item)
            if c == 2:
              ov = item
          
          if pairval > ov:
            return 1
          elif pairval < ov:
            return 0
          else:
            ss = sorted(list(set(self.vals)))
            os = sorted(list(set(other.vals)))
​
            for n in range(1, len(ss) + 1):
              si = ss[-n]
              oi = os[-n]
​
              if si>oi:
                return 1
              elif si < oi:
                return 0
           # print(self.vals, other.vals)
            return 0
        else:
          ss = sorted(list(set(self.vals)))
          os = sorted(list(set(other.vals)))
​
          for n in range(1, len(ss) + 1):
            si = ss[-n]
            oi = os[-n]
​
            if si > oi:
              return 1
            elif si < oi:
              return 0
          
          #print(self.vals, other.vals)
          return 0
​
​
​
  player1 = {}
  player2 = {}
  
  for n in range(len(lst)):
    ll = lst[n].split()
​
    p1 = ll[:5]
    p2 = ll[5:]
​
    player1[n] = Hand(p1)
    player2[n] = Hand(p2)
  
  p1_wins = 0
​
  for n in range(len(lst)):
    win = player1[n].versus(player2[n])
    p1_wins += win
    #print(player1[n].hand, player2[n].hand, win)
  
  return p1_wins

