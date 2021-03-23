"""


Primiera (from the french word _prime_ , "prize") is a combination of cards of
_Scopa_ , a popular Italian card game.

For establishing the value of the Primiera, a separate point scale is used for
selecting the best cards in the player's deck, in each of the four suits and
totaling those four cards point values. A Primiera requires at least one card
for each suit, otherwise, it can't be calculated.

This is the Primiera points scale:

  * 7 is worth 21 points.
  * 6 is worth 18 points.
  * Ace is worth 16 points.
  * Cards from 2 to 5 are worth 10 points plus the card value.
  * Face cards (Jack, Queen and King) are worth 10 points.

Create a function that takes in a list representing a cards deck and returns
the value of the Primiera.

### Examples

    get_primiera_score(["Ad", "7d", "5h", "2c", "Ks"]) ➞ 58
    # In the diamonds set 7 is higher than Ace (21 > 16).
    
    get_primiera_score(["2d", "Jd", "7h", "Qc", "5s", "As"]) ➞ 59
    # In the diamonds set 2 is higher than Jack (12 > 10), while in
    # the spades set Ace is higher than 5 (16 > 15 ).
    
    get_primiera_score(["2d", "Jd", "Qc", "5s", "As"]) ➞ 0
    # There aren't cards in the hearts set, so Primiera can't be
    # calculated.

### Notes

  * Notation: **A** ce, card numbers from **2 to 7** , **J** ack, **Q** ueen or **K** ing + **d** iamonds, **h** earts, **c** lubs or **s** pades.
  * If one or more seeds are missing from the deck the value of the Primiera is equal to 0.

"""

def points(card):
  card=card[0]
  if card.isalpha(): return 10+6*(card=='A')
  if card<'6': return int(card)+10
  return 18+3*(card=='7')
​
def get_primiera_score(deck):
  if len(set([i[1] for i in deck]))!=4: return 0
  d={'h': [], 's': [], 'c': [], 'd': []}
  for i in deck: d[i[1]].append(points(i))
  return sum([max(d[i]) for i in d])

