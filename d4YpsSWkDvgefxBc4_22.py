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
  Vals = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10, "A":11}
  total = sum([Vals[i] for i in cards])
  if "A" in cards and total> 12:
    total -= 10
  return total > 21

