"""


This is a reverse-coding challenge. Create a function that outputs the correct
list from the input. Use the following examples to crack the code.

### Examples

    decode("hello") ➞ [5, 2, 9, 9, 3]
    
    decode("wonderful") ➞ [11, 3, 2, 1, 2, 6, 3, 9, 9]
    
    decode("something challenging") ➞ [7, 3, 10, 2, 8, 5, 6, 2, 4, 5, 18, 5, 16, 9, 9, 2, 2, 4, 6, 2, 4]

### Notes

N/A

"""

def decode(txt):
  lookup = {" ":5, "R":10, "a":16, "b":17, "c":18, "d":1, "e":2, "f":3, "g":4, "h":5, "i":6, "j":7, "k":8, "l":9, "m":10, "n":2, "o":3, "p":4, "q":5, "r":6, "s":7, "t":8, "u":9, "v":10, "w":11, "x":12, "y":4, "z":14}
  lst = []
  for x in txt:
    lst.append(lookup.get(x))
  return lst

