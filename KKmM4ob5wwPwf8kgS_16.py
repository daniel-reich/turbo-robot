"""


Create a function that returns the frequency distribution of a list. This
function should return an object, where the keys are the unique elements and
the values are the frequency in which those elements occur.

### Examples

    get_frequencies(["A", "B", "A", "A", "A"]) ➞ { "A" : 4, "B" : 1 }
    
    get_frequencies([1, 2, 3, 3, 2]) ➞ { 1: 1, 2: 2, 3: 2 }
    
    get_frequencies([True, False, True, False, False]) ➞ { True: 2, False: 3 }
    
    get_frequencies([]) ➞ {}

### Notes

  * If given an empty list, return an empty object (see example #4).
  * The object should be in the same order as in the input list.

"""

def get_frequencies(lst):
  dic={}
  for x in lst:
    if x in dic:
      dic[x]=dic[x]+1
    else:
      dic[x]=1
  return dic

