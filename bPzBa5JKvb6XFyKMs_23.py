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

def valid(lst):
    d = {'c': 0,'d': 0,'h': 0, 's':0}
    for card in lst:
        suit = card[1]
        if suit in d:
            d[suit] += 1
    return False if min(d.values()) == 0 else True
​
def maxCard(lst,dict):
    if len(lst) == 1:
        if lst[0] in dict:
            if(lst[0][0].isdigit() and int(lst[0][0]) >= 2 and int(lst[0][0]) <= 5):
                return dict[lst[0]] + int(lst[0][0])
            else:
                return dict[lst[0]]
    else:
        card_scores = {}
        for card in lst:
            if(card[0].isdigit() and int(card[0]) >= 2 and int(card[0]) <= 5):
                card_scores[card] = dict[card] + int(card[0])
            else:
                card_scores[card] = dict[card]
​
        return max(card_scores.values())
​
def get_primiera_score(lst):
    #clubs, diamonds, herats, spades
    points_scale = {
    '2c': 10, '3c': 10, '4c': 10, '5c': 10, '6c': 18, '7c': 21, 'Ac': 16, 'Jc': 10, 'Kc': 10, 'Qc': 10,
    '2d': 10, '3d': 10, '4d': 10, '5d': 10, '6d': 18, '7d': 21, 'Ad': 16, 'Jd': 10, 'Kd': 10, 'Qd': 10,
    '2h': 10, '3h': 10, '4h': 10, '5h': 10, '6h': 18, '7h': 21, 'Ah': 16, 'Jh': 10, 'Kh': 10, 'Qh': 10,
    '2s': 10, '3s': 10, '4s': 10, '5s': 10, '6s': 18, '7s': 21, 'As': 16, 'Js': 10, 'Ks': 10, 'Qs': 10 }
​
    clubs = []
    diamonds = []
    hearts = []
    spades = []
​
    if(not valid(lst)):
        return 0
    else:
        #calculate the primiera score
        for card in lst:
            if(card.endswith('c')):
                clubs.append(card)
            elif(card.endswith('d')):
                diamonds.append(card)
            elif(card.endswith('h')):
                hearts.append(card)
            elif(card.endswith('s')):
                spades.append(card)
​
        scores = [maxCard(clubs,points_scale), maxCard(diamonds,points_scale), maxCard(hearts,points_scale), maxCard(spades,points_scale)]
​
    return sum(scores)

