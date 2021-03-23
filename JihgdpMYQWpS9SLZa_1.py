"""


Your goal is to know the score of the hand, either by getting three cards of
the same rank (like 8s or Jacks) or the same suit (e.g. hearts(H) or
spades(S)). The value of your hand is calculated by adding up the total of
your cards in any one suit.

Regular cards are worth their number, face cards are worth 10, and Aces are
worth 11, but remember, **only one of your suits counts**! You can also make a
hand of **three cards with the same rank** , like 8-8-8 or J-J-J. This is
worth 30.5 points unless it is A-A-A, which is worth 32.

Take three strings: **c1, c2, and c3** and return a number **score**.

### Examples

    score31("CA", "D9", "H8") ➞ 11
    
    score31("SJ", "SQ", "S8") ➞ 28
    
    score31("DA", "DK", "DQ") ➞ 31

### Notes

  * Cards are of these suits: H-hearts, C-clubs, S-spades, and D-diamonds.
  * Numbers are: 7, 8, 9, 10, J, Q, K, A

"""

def score31(*args):
    set_val = set(card[-1] for card in args)
    if len(set_val) == 1:
        if set_val == {"A"}:
            return 32
        return 30.5
​
    suit = {"H": 0, "C": 0, "S": 0, "D": 0}
    face = {"A": 11, "K": 10, "Q": 10, "J": 10}
    for card in args:
        value = card[1:]
        if value in face:
            suit[card[0]] += face[value]
        else:
            suit[card[0]] += int(value)
    return max(suit.values())

