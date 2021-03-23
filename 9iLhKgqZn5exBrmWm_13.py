"""


Write a function that returns `True` if a string consists of **ascending or
ascending AND consecutive** numbers.

### Examples

    ascending("232425") ➞ True
    # Consecutive numbers 23, 24, 25
    
    ascending("2324256") ➞ False
    # No matter how this string is divided, the numbers are not consecutive.
    
    ascending("444445") ➞ True
    # Consecutive numbers 444 and 445.

### Notes

A **number** can consist of any number of digits, so long as the numbers are
adjacent to each other, and the string has at least two of them.

"""

def ascending(txt):
  max_digits = len(txt) // 2
  # The starting number in the sequence could be any number of digits,
  # up to half of the length of 'txt'
  for digits in range(1, max_digits+1):
    index = 0  # Keeps track of where we are in 'txt'
    expected = txt[:digits]
    while True:
      num = txt[index:index + digits]
      # If the next number encountered isn't the next consecutive number,
      # move on and try to start with more digits
      if num != expected:
        break
      # We got the next consecutive number, advance the index
      index += digits
      # If we made it exactly to the end of txt, these were all
      # consecutive numbers, and we are done
      if index == len(txt):
        return True
      # If we aren't yet at the end of the string, determine the next
      # number in the sequence, and the number of digits in it
      expected = str(int(num) + 1)
      digits = len(expected)
  # If we looped through all possible starting numbers and didn't find
  # a match, this isn't a string of consecutive numbers
  return False

