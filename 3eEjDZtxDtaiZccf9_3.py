"""


This question is inspired by the popular Uno card game.

Write a function that takes in two arguments: (1) a player's current hand and
(2) the current face-up card on the table. The function will return `True` if
the player can make a play, or `False` if the player has to draw from the
deck.

A player can make a play if either:

  * They have a card that is the same **color** as the face-up card.
  * They have a card that is the same **number** as the face-up card.

    can_play(["yellow 3", "yellow 7", "blue 8", "red 9", "red 2"], "red 1") ➞ True
    # Since the player has two red cards, and the face-up card is red.
    
    can_play(["yellow 3", "yellow 7"], "blue 7") ➞ True
    # Since the player has a 7, and the face-up card is a 7.

### Examples

    can_play(["yellow 3", "yellow 5", "red 8"], "red 2") ➞ True
    
    can_play(["yellow 3", "yellow 5", "red 8"], "blue 5") ➞ True
    
    can_play(["yellow 3", "blue 5", "red 8", "red 9"], "green 4") ➞ False
    
    can_play(["yellow 3", "red 8"], "green 2") ➞ False

### Notes

  * Return `False` if the player is not holding any cards (an empty list). 
  * There are no special cards or wild cards in this deck.

"""

def can_play(hand, face):
  atts = sum([x.split() for x in hand],[])
  return any([x in face.split() for x in atts])

