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
  sums=[]
  for i in range(0,len(lst)):
    total=0
    for k in range(0,len(lst[i])):
      total+=ord(lst[i][k])
    sums.append(total)
  if sums[0] < sums[1]:
    small=lst[0]
  else:
    small=lst[i]
  return small

