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
  lst2 = []
  count = 0
  for i in lst:
    count = 0
    for j in i:
      count += ord(j)
    lst2.append(count)
  if lst2[0] < lst2[1]:
    return lst[0]
  else:
    return lst[1]

