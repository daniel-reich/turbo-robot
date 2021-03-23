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

def numberSequence(n, goal = None, asc_desc = 'd', two_ones = None):
  
  if n <= 0:
    return '-1'
    
  if goal == None:
    if n % 2 == 0:
      goal = n // 2
      two_ones = True
    else:
      goal = (n // 2) + 1
      two_ones = False
  
  if goal == 1:
    if n == 1:
      return '1'
    if n == 2:
      return '1 1'
  
  if asc_desc == 'd':
    
    if n == 1:
      if two_ones == True:
        return '1 1 ' + numberSequence(n + 1, goal, 'a', two_ones)
      else:
        return '1 ' + numberSequence(n + 1, goal, 'a', two_ones)
    elif n > goal:
      return numberSequence(goal, goal, asc_desc, two_ones)
    else:
      return str(n) + ' ' + numberSequence(n - 1, goal, asc_desc, two_ones)
  
  else:
    if n == goal:
      return str(n)
    else:
      return str(n) + ' ' + numberSequence(n + 1, goal, asc_desc, two_ones)

