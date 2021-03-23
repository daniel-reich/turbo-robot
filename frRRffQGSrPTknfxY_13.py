"""


Given a number, create a function that returns a new number based on these
rules:

  * For each digit, replace it by the number of times it appears in the number.
  * The final instance of the number will be an integer, not a string.

### Worked Example

    digit_count(136116) ➞ 312332
    # The number 1 appears thrice, so replace all 1s with 3s.
    # The number 3 appears only once, so replace all 3s with 1s.
    # The number 6 appears twice, so replace all 6s with 2s.
    # Return as an integer.

### Examples

    digit_count(221333) ➞ 221333
    
    digit_count(136116) ➞ 312332
    
    digit_count(2) ➞ 1

### Notes

All test input will be positive whole numbers.

"""

def digit_count(n):
  freqchar = {}
  stringn = str(n)
  for char in stringn:
    if char not in freqchar:
      freqchar[char] = 1
    elif char in freqchar:
      freqchar[char] += 1
  
  newnumber = 0
  for char in stringn:
    newdigit = int(freqchar[char])
    newnumber = newnumber * 10 + newdigit
  
  return newnumber

