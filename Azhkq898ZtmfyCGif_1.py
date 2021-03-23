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
  if not lst:
    return []
  else:
    if len(lst)==1:
      return [str(lst[0])]
    else:
      A=[]
      for i in range(len(lst)-1):
        if lst[i+1]-lst[i]!=1:
          A.append(lst[i])
          A.append(lst[i+1])
      if not A:
        return [str(lst[0])+'-'+str(lst[-1])]
      else:
        if lst[0]==A[0]:
          return [str(lst[0]), str(A[-1])+'-'+str(lst[-1])]
        return [str(lst[0])+'-'+str(A[0]), str(A[-1])+'-'+str(lst[-1])]

