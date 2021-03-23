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
  parse_suit = lambda card: card[-1]
  table_suit_list = list(map(parse_suit,table))
  for table_suit in table_suit_list:
    numSuit_table = table_suit_list.count(table_suit)
    if numSuit_table + list(map(parse_suit,hand)).count(table_suit) >= 5:
        return True
  return False

