"""


Create a function that takes two lists and combines them by alternatingly
taking elements from each list in turn.

  * The lists may be of different lengths, with at least one character / digit.
  * The first list will contain string characters (lowercase, a-z).
  * The second list will contain integers (all positive).

### Examples

    merge_arrays(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5])
    ➞ ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5]
    
    merge_arrays([1, 2, 3], ["a", "b", "c", "d", "e", "f"])
    ➞ [1, "a", 2, "b", 3, "c", "d", "e", "f"]
    
    merge_arrays(["f", "d", "w", "t"], [5, 3, 7, 8])
    ➞ ["f", 5, "d", 3, "w", 7, "t", 8]

### Notes

N/A

"""

def merge_arrays(a, b):
  
  result = []
  k = len(a)
  m = len(b)
  
  for x in range(max(k, m)):
    try:
      result.append(a[x])
    except:
      pass
    try:
      result.append(b[x])
    except:
      pass
  
  return result

