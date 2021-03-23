"""


Create a function that takes a list of numbers and return its median. If the
input list is even length, take the average of the two medians, else, take the
single median.

### Examples

    median([2, 5, 6, 2, 6, 3, 4]) ➞ 4
    
    median([21.4323, 432.54, 432.3, 542.4567]) ➞ 432.4
    
    median([-23, -43, -29, -53, -67]) ➞ -43

### Notes

  * Input can be any negative or positive number.
  * Input list will contain at least four numbers.
  * See **Resources** tab for info on calculating the median.

"""

def median(lst):
  lst.sort()
  if len(lst) % 2:
    return lst[int(len(lst) / 2)]
  else:
    return (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1] ) /2

