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
  sum1=0
  sum2=0
  for x in lst[0]:
    sum1+=ord(x)
  for x in lst[1]:
    sum2+=ord(x)
  return lst[0] if sum1<sum2 else lst[1]

