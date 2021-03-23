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

def over_twenty_one(lst):
  lst_value = [10 for nums in lst if nums in ["K", "Q", "J"]]
  num_value = [num for num in lst if num in range(1,11)]
  if "A" in lst and (sum(lst_value) + sum(num_value)) <= 20:
    total = sum(lst_value) + sum(num_value) + 1
  elif "A" in lst and (sum(lst_value) + sum(num_value)) <= 10:
    total = sum(lst_value) + sum(num_value) + 11
  else:
    total = sum(lst_value) + sum(num_value)
  return total > 21

