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
  bitstring_list = convert_to_bitstring(word)
  newlist = []
  for eachpart in bitstring_list:
    if eachpart == 1:
      newlist.append(True)
    else:
      newlist.append(False)
  return newlist
  
  
def convert_to_bitstring(word):
  word = word.lower()
  alphabet = ' abcdefghijklmnopqrstuvwxyz'
  newlist = []
  for eachletter in word:
    if alphabet.index(eachletter) % 2 != 0:
      newlist.append(1)
    else:
      newlist.append(0)
  return newlist

