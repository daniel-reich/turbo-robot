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

def calcScore(v):
    if v == 'A':
        return 16
    if v == 'K' or v == 'Q' or v == 'J':
        return 10
    if 2 <= int(v) <= 5:
        return 10+int(v)
    if v == '6':
        return 18    
    if v == '7':
        return 21
    
def get_primiera_score(deck):
    #[Hearts,Diamonds,Spades,Clubs]
    myScore = [-1,-1,-1,-1]
    
    for item in deck:
        if item[1] == 'h':
            s = calcScore(item[0])
            if s > myScore[0]:
                myScore[0] = s   
        elif item[1] == 'd':
            s = calcScore(item[0])
            if s > myScore[1]:
                myScore[1] = s
        elif item[1] == 's':
            s = calcScore(item[0])
            if s > myScore[2]:
                myScore[2] = s
        else:
            s = calcScore(item[0])
            if s > myScore[3]:
                myScore[3] = s            
    if -1 in myScore:
        return 0
    else:
        return sum(myScore)

