"""


Write a function that returns the largest even integer in a list with its
corresponding index and the parity of that index, but determining the parity
of that index is **limited to not using** the **modulo operator** `%`.

### Output Structure:

    {"@odd|even index " + index_of_largest: largest_integer}

### Examples

    bitwise_index([107, 19, 36, -18, -78, 24, 97]) ➞ {"@even index 2": 36}
    
    bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]) ➞ {"@even index 6": 10}
    
    bitwise_index([4, 4, 4, 4, 4, 4]) ➞ {"@even index 0": 4}
    
    bitwise_index([-31, -7, -13, -7, -9, -13]) ➞ "No even integer found!"

### Notes

  * The use of `index()` and `max()` are restricted.
  * If there are no even integers, return `"No even integer found!"`.
  * The set of limitations imposed on this challenge dictates the level of difficulty.
  * Another version of this challenge that deals with recursion can be [found here](https://edabit.com/challenge/pMbki4f2BA8R5vbXs).

"""

def bitwise_index(lst):
 e = [i for i in lst if str(i)[len(str(i))-1] in list("02468")]
 if len(e) == 0:
  return "No even integer found!"
 else:
  em = (sorted(e))[len(e)-1]
  ind = [i for i in range(len(lst)) if lst[i] == em][0]
  if str(ind)[len(str(ind))-1] in list("02468"):
    return {"@even index "+str(ind): em}
  if str(ind)[len(str(ind))-1] in list("13579"):
    return {"@odd index "+str(ind): em}

