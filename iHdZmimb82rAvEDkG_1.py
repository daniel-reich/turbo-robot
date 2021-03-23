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
  def is_even(n):
    string = str(n)
    return string[-1] in '24680'
  
  def highest_even(lst):
    even = []
    
    for n in lst:
      if is_even(n) == True:
        even.append(n)
    try:
      return max(even)
    except:
      return None
  
  he = highest_even(lst)
  
  def find_index(item, lst):
    for n in range(len(lst)): 
      try:
        if lst[n] == item:
          #print(n)
          return n
      except IndexError:
        pass
    return False
  
  if he == None:
    return 'No even integer found!'
  
  fi = find_index(he, lst)
  index_parity = is_even(fi)
  
  if index_parity == True:
    index_parity = 'even'
  else:
    index_parity = 'odd'
    
  return {'@{} index {}'.format(index_parity, fi): he}

