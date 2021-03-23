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
  dict = {}
  for i in range(0, len(lst)):
    rep = 0
    for j in range(0, len(lst)):
      if (lst[i] == lst[j]):
        rep += 1 
    dict[lst[i]] = rep
  return dict

