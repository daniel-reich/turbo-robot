"""


Create a function that takes both a string and a list of integers and
rearranges the letters in the string to be in the order specified by the index
numbers. Return the "remixed" string.

### Examples

    remix("abcd", [0, 3, 1, 2]) ➞ "acdb"

The string you'll be returning will have:

  * "a" at index 0
  * "b" at index 3
  * "c" at index 1
  * "d" at index 2

... because the order of those characters maps to their corresponding numbers
in the index list.

    remix("PlOt", [1, 3, 0, 2]) ➞ "OPtl"
    
    remix("computer", [0, 2, 1, 5, 3, 6, 7, 4]) ➞ "cmourpte"

### Notes

  * Be sure not to change the original case.
  * Assume you'll be given a string and list of equal length, both containing valid characters (A-Z, a-z, or 0-9).
  * The list of numbers could potentially be more than nine (i.e. double figures).

"""

def remix(txt, lst):
  result = [None]*len(txt)
  for character, position in zip(txt, lst):
    result[position] = character
  return ''.join(result)

