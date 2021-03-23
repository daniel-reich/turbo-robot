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

values = {'A': 11, 'J': 10, 'Q': 10, 'K': 10, '7': 7, '8': 8, '9': 9, '10': 10}
​
def score31(c1, c2, c3):
    ranks = [c[1:] for c in [c1, c2, c3]]
    score3 = 0
    if len(set(ranks)) == 1:
        score3 = 32 if ranks[0] == 'A' else 30.5
    score_suit = 0
    for suit in "CDHS":
        score = 0
        for c in [c1, c2, c3]:
            if c[0] == suit:
                score += values[c[1:]]
        score_suit = max(score_suit, score)
    return max(score_suit, score3)

