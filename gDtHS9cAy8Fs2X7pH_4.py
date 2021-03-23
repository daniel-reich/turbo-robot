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
  a = sorted([[i, lst.count(i)] for i in set(lst)], key=lambda x: x[1])
  return {i[0]:i[1] for i in a[::-1]}

