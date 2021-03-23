"""


Create a function that takes two parameters (`start`, `stop`), and returns the
sum of all even numbers in the range.

### Examples

    sum_even_nums_in_range(10, 20) ➞ 90
    # 10, 12, 14, 16, 18, 20
    
    sum_even_nums_in_range(51, 150) ➞ 5050
    
    sum_even_nums_in_range(63, 97) ➞ 1360

### Notes

Remember that the `start` and `stop` values are inclusive.

"""

def sum_even_nums_in_range(start, stop):
  if start % 2 == 0:
    return sum([i for i in range(start,stop+1,2)])
  else:
    return sum([i for i in range(start+1,stop+1,2)])
