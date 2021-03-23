"""


Create a function that takes in two lists and determines whether there exists
a flush.

  * The first list represents the 5 cards dealt on the table.
  * The second list represents the 2 cards in your hand.

Notation: card number and suit (abbreviated as S = Spades, H = Hearts, D =
Diamonds, C = Clubs) separated by an underscore.

### Examples

    check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]) ➞ True // diamond flush
    
    check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]) ➞ True // spade flush
    
    check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]) ➞ False

### Notes

Hint: If there aren't at least 3 cards of the same suit on the table, there is
zero chance of there being a flush.

"""

def check_flush(table, hand):
  def table_check(t):
    suits = []
​
    for card in table:
      c = card.split('_')
      num = c[0]
      suit = c[1]
​
      suits.append(suit)
    
    pos = False
    imp_suit = None
​
    for suit in suits:
      c = suits.count(suit)
      if c >= 3:
        pos = True
        imp_suit = suit
        break
    
    return [pos, imp_suit]
  def hand_check(h):
    suits = []
    for card in h:
      c = card.split('_')
      num = c[0]
      suit = c[1]
​
      suits.append(suit)
    
    c = suits.count(suits[0])
​
    if c == 2:
      return [True, suits[0]]
    else:
      return False
  
  tc = table_check(table)
  if tc == False:
    return False
  hc = hand_check(hand)
  if hc == False:
    return False
  else:
    table_suit = tc[1]
    hand_suit = hc[1]
    
    if table_suit == hand_suit:
      return True
    else:
      return False

