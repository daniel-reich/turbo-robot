"""


In this challenge, you have to establish if the digits of a given number form
a straight arithmetic sequence (either increasing or decreasing). A straight
sequence has an equal step between every pair of digits.

Given an integer `n`, implement a function that returns:

  * `"Not Straight"` if `n` is lower than 100 or if its digits are not an arithmetic sequence.
  * `"Trivial Straight"` if `n` has a single repeating digit.
  * An integer being the step of the sequence if the `n` digits are a straight arithmetic sequence.

### Examples

    straight_digital(123) ➞ 1
    # 2 - 1 = 1 | 3 - 2 = 1
    
    straight_digital(753) ➞ -2
    # 5 - 7 = -2 | 3 - 5 = -2
    
    straight_digital(666) ➞ "Trivial Straight"
    # There's a single repeating digit (step = 0).
    
    straight_digital(124) ➞ "Not Straight"
    # 2 - 1 = 1 | 4 - 2 = 2
    # A valid sequence has always the same step between its digits.
    
    straight_digital(99) ➞ "Not Straight"
    # The number is lower than 100.

### Notes

  * The step of the sequence can be either positive or negative (see example #2).
  * Trivia: there are infinite straight digital numbers, but only 96 of them are made of at least two different digits.

"""

def straight_digital(number):
  if number < 100:
    return "Not Straight"
  number = str(number)[::-1]
  if number.count(number[0]) == len(number):
    return "Trivial Straight"
  step = ord(number[0]) - ord(number[1])
  for foo in range(1, len(number) - 1):
    if (ord(number[foo]) - ord(number[foo + 1])) != step:
      return "Not Straight"
  return step

