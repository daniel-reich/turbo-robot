"""


Write a **recursive** function that accepts an integer `n` and return a
sequence of `n` integers as a string, descending from `n` to 1 and then
ascending back from 1 to `n` as in the examples below:

### Examples

    number_sequence(1) ➞ "1"
    
    number_sequence(2) ➞ "1 1"
    
    number_sequence(3) ➞ "2 1 2"
    
    number_sequence(4) ➞ "2 1 1 2"
    
    number_sequence(9) ➞ "5 4 3 2 1 2 3 4 5"
    
    number_sequence(10) ➞ "5 4 3 2 1 1 2 3 4 5"

### Notes

  * Only use recursion.
  * No auxiliary data structures like list and tuple are allowed.

"""

def numberSequence(n,lst=[1]):
  if n<1:
    return '-1'
  elif len(lst)==n:
    return ' '.join([str(i) for i in lst])
  elif lst[-1]>n//2:
    return numberSequence(n,[lst[0]+1]+lst)
  elif n%2==0 and lst[-1]==n//2:
    if len(lst)==n//2:
      return numberSequence(n,[1]+lst)
    else:
      return numberSequence(n,[lst[0]+1]+lst)
  return numberSequence(n,lst+[lst[-1]+1])

