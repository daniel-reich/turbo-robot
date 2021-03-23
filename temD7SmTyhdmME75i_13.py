"""


Create a function that converts a word to a bitstring and then to a boolean
list based on the following criteria:

  1. Locate the position of the letter in the English alphabet (from 1 to 26).
  2. Odd positions will be represented as `1` and `0` otherwise.
  3. Convert the represented positions to boolean values, `1` for `True` and `0` for `False`.
  4. Store the conversions into an array.

### Examples

    to_boolean_list("deep") ➞ [False, True, True, False]
    # deep converts to 0110
    # d is the 4th alphabet - 0
    # e is the 5th alphabet - 1
    # e is the 5th alphabet - 1
    # p is the 16th alphabet - 0
    
    to_boolean_list("loves") ➞ [False, True, False, True, True]
    
    to_boolean_list("tesh") ➞ [False, True, True, False]

### Notes

  * The letter `A` is at position `1` and `Z` at `26`.
  * All input strings are in lowercase letters of the English alphabet.

"""

def to_boolean_list(word):
  lst1=[]
  lst2=[]
  for i in word:
      if (ord(i)-64)%2==0:
          lst1.append(0)
      else:
          lst1.append(1)
  for i in lst1:
      if i==1:
          lst2.append(True)
      else:
          lst2.append(False)
  return lst2

