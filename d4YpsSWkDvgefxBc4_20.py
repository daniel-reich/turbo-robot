"""


Create a function that takes a list of card numbers and checks if the sum of
their value exceeds 21. If the sum exceeds 21, return `True` and if the sum is
under or equal to 21, return `False`. Values of the cards are as follows:

  * 2-10 are their value.
  * J-K (face cards) count as 10.
  * Aces count either as 1 or 11 - play conservatively, so that if giving an ace a value of 11 causes you to lose and 1 allows you to win, then go with 1.

### Examples

    over_twenty_one([2, 8, "J"]) ➞ False
    
    over_twenty_one(["A", "J", "K"]) ➞ False
    
    over_twenty_one([5, 5, 3, 9]) ➞ True
    
    over_twenty_one([2, 6, 4, 4, 5]) ➞ False
    
    over_twenty_one(["J", "Q", "K"]) ➞ True

### Notes

There will be a maximum of one ace in each hand.

"""

def over_twenty_one(cards):
  sum_card = 0
  for card in cards:
    if type(card) == int:
      sum_card += card
    elif card in ["J", "K", "Q"]:
      sum_card += 10
  if "A" in cards:
    if sum_card + 11 > 21:
      if sum_card + 1 <= 21:
        return False
      else:
        return True
  if sum_card > 21:
    return True
  else:
    return False

