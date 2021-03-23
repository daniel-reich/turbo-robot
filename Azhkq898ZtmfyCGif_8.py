"""


Create a function which converts an **ordered** number list into a list of
ranges (represented as strings). Note how some lists have some numbers
missing.

### Examples

    numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]
    
    numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]
    
    numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]
    
    numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]

### Notes

  * If there are no numbers consecutive to a number in the list, represent it as only the _string_ version of that number (see example #4).
  * Return an empty list if the given list is empty.

"""

from itertools import takewhile
def numbers_to_ranges(lst):
  def ranges(newlst,lst):
    if not lst:
      return newlst
    else:
      lst2 = list(takewhile(lambda x: x[0] == x[1], zip(lst,list(range(lst[0],len(lst) + lst[0])))))
      lower = lst2[0][0]
      higher = lst2[-1][0]
      if lower == higher:
        newlst.append(str(lower))
      else:
        newlst.append("{}-{}".format(str(lower),str(higher)))
      return newlst if lst[-1] == higher else ranges(newlst,lst[lst.index(higher)+1::])
  return ranges([],lst)

