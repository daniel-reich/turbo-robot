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
  res = []; temp = []
  for i in range(len(lst)):
    if not temp:
      temp.append(lst[i])
    elif lst[i] == temp[-1] + 1:
      temp.append(lst[i])
    else:
      res.append(temp)
      temp = [lst[i]]
  if temp:
    res.append(temp)
  return ['{}-{}'.format(i[0],i[-1]) if len(i) > 1 else str(i[0]) for i in res]

