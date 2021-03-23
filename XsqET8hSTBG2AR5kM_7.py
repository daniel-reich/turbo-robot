"""


Given two words, the **letter distance** is calculated by taking the absolute
value of the difference in character codes and summing up the difference.

If one word is longer than another, add the difference in lengths towards the
score.

To illustrate:

    letter_distance("house", "fly") = dist("h", "f") + dist("o", "l") + dist("u", "y") + dist(house.length, fly.length)
    
    = |104 - 102| + |111 - 108| + |117 - 121| + |5 - 3|
    = 2 + 3 + 4 + 2
    = 11

### Examples

    letter_distance("sharp", "sharq") ➞ 1
    
    letter_distance("abcde", "Abcde") ➞ 32
    
    letter_distance("abcde", "bcdef") ➞ 5

### Notes

  * Always start comparing the two strings from their first letter.
  * Excess letters are not counted towards distance.
  * Capital letters are included.

"""

def letter_distance(txt1, txt2):
  if len(txt1) > len(txt2):
    n = len(txt2)
  else:
    n = len(txt1)
  return sum(abs(ord(txt1[i]) - ord(txt2[i])) for i in range(n)) + abs(len(txt1) - len(txt2))

