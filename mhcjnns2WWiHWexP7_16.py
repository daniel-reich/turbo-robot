"""


In a board game, a player may pick up a card with several left or right facing
arrows, with the number of arrows indicating the number of tiles to move. The
player should move either left or right, depending on the arrow's direction.

Given a list of the arrows contained on a player's cards, return a singular
string of arrowheads that are equivalent to all of the arrowheads.

### Worked Example

    calculate_arrowhead([">>", "<<", "<<<"]) ➞ "<<<"
    
    # >> means to move 2 places right
    # << means to move 2 places left (cancelling out >>)
    # <<< means to move a further 3 places left
    # overall, the movement can be written as <<<

### Examples

    calculate_arrowhead([">>>>", "<", "<", "<"]) ➞ ">"
    
    calculate_arrowhead([">", "<", ">>", "<", "<<<"]) ➞ "<<"
    
    calculate_arrowhead([">>>", "<<<"]) ➞ ""

### Notes

Return an **empty string** if all the arrowheads cancel out.

"""

def calculate_arrowhead(lst):
    if isinstance(lst, list):
        #print("Het is een list")
        pass
    else:
        print("het is geen list, maar een {}".format(type(lst)))
    aantal_zetten = len(lst)
    #print("aantal zetten is {}".format(aantal_zetten))
​
    verplaatsing = 0
    for zet in lst:
        #print(zet)
        if '<' in zet:
            #print("Links")
            verplaatsing -= len(zet)
        elif '>' in zet:
            #print("Rechts")
            verplaatsing += len(zet)
        else:
            print("Foute input!")
    
    #print("De verplaatsing is {}".format(verplaatsing))
    if verplaatsing < 0:
        visueel = abs(verplaatsing) * '<'
        #print("Links")
    elif verplaatsing > 0:
        #print("Rechts")
        visueel = verplaatsing * '>'
    elif verplaatsing == 0:
        #print("Blijf staan...")
        visueel = ''
    return visueel

