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

def get_total(str):
    total = 0
    for char in str:
        total += ord(char)
​
    return total
​
def ascii_sort(lst):
  min_total = get_total(lst[0])
  min_str = lst[0]
  for str in lst:
    if min_total > get_total(str):
      min_total = get_total(str)
      min_str = str
  return min_str

