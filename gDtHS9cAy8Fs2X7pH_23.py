"""


Given a list, create a function that returns a dictionary detailing how many
times each element was repeated.

### Examples

    count_repetitions(["cat", "dog", "cat", "cow", "cow", "cow"]) ➞ { cow: 3, cat: 2, dog: 1 }
    
    count_repetitions([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0]) ➞ { 0: 6, 5: 3, 12: 2, 1: 1 }
    
    count_repetitions(["Infinity", "null", "Infinity", "null", "null"]) ➞ { "null": 3, "Infinity": 2}

### Notes

N/A

"""

def count_repetitions(lst):
  dic1 = {}
  for i in lst:
    if i not in dic1:
      dic1[i] = 1
    else:
      x = dic1[i]
      x += 1
      dic1[i] = x
  return dic1

