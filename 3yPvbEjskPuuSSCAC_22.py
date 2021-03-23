"""


Given a list of numbers, remove the largest and smallest numbers, and
calculate the average of the remaining numbers.

### Examples

    trimmed_averages([4, 5, 7, 100]) ➞ 6
    # Average of 5 and 7
    
    trimmed_averages([10, 25, 5, 15, 20]) ➞ 15
    # Average of 10, 15 and 20
    
    trimmed_averages([1, 1, 1]) ➞ 1
    # 1

### Notes

  * Round to the nearest whole number.
  * List size is greater than 2.

"""

def trimmed_averages(lst):
  lst = sorted(lst)
  lst.remove(max(lst))
  lst.remove(min(lst))
  return round(sum(lst)/len(lst))

