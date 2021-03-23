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
  if(lst == []): return []
  lenLst = len(lst)
  currRange = [str(lst[0]),'-',None]
  rangeList = []
  for i in range(lenLst):
    if(i == lenLst-1):
      if(currRange[2] == None):
        rangeList.append(currRange[0])
      else:
        rangeList.append(currRange[0]+currRange[1]+currRange[2])
    elif(lst[i+1] == lst[i]+1):
      currRange[2] = str(lst[i+1])
    else:
      if(currRange[2] == None):
        rangeList.append(currRange[0])
      else:
        rangeList.append(currRange[0]+currRange[1]+currRange[2])
      currRange = [str(lst[i+1]),'-',None]
  return rangeList

