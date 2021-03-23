"""


Create a function that compares two words based on the sum of their ASCII
codes and returns the word with the smaller ASCII sum.

### Examples

    ascii_sort(["hey", "man"]) ➞ "man"
    # ["h", "e", "y"] ➞ sum([104, 101, 121]) ➞ 326
    # ["m", "a", "n"] ➞ sum([109, 97, 110]) ➞ 316
    
    ascii_sort(["majorly", "then"]) ➞ "then"
    
    ascii_sort(["victory", "careless"]) ➞ "victory"

### Notes

Both words will have strictly different ASCII sums.

"""

def ascii_sort(lst):
  word1 = lst[0]
  word2 = lst[1]
  word1 = list(word1)
  word2 = list(word2)
  sum1 = 0
  sum2 = 0
  for char in word1:
    sum1 += ord(char)
  for char in word2:
    sum2 += ord(char)
  if sum1 < sum2:
    return "".join(word1)
  else:
    return "".join(word2)

