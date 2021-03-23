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
  sum_of_word_one = 0
  sum_of_word_two = 0
  for char in lst[0]:
    sum_of_word_one += ord(char)
  for char in lst[1]:
    sum_of_word_two += ord(char)
  return lst[0] if sum_of_word_one < sum_of_word_two else lst[1]

