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

def numbers_to_ranges(lst):
  it1,it2,ret = 0,0,[]
  while it2<len(lst):
    if it2<len(lst)-1 and lst[it2]+1==lst[it2+1]:
      it2+=1
    else:
      if it1==it2:
        ret.append(str(lst[it1]))
      else:
        ret.append(str(lst[it1])+'-'+str(lst[it2]))
      it1,it2 = it2+1,it2+1
  return ret

