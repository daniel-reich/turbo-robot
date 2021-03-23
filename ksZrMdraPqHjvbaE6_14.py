"""


Write a function that finds the **largest even number** in a list. Return `-1`
if not found. The use of built-in functions `max()` and `sorted()` are
prohibited.

### Examples

    largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10
    
    largest_even([1, 3, 5, 7]) ➞ -1
    
    largest_even([0, 19, 18973623]) ➞ 0

### Notes

Consider using the **modulo operator** `%` or the **bitwise and operator**
`&`.

"""

def largest_even(lst):
  
  Evens = []
  
  for x in lst:
    if (x % 2 == 0):
      Evens.append(x)
  
  Counter = 0
  Length = len(Evens)
  Outcome = -1
  
  while (Counter < Length):
    
    Attempt = Evens[Counter]
    
    if (Attempt > Outcome):
      Outcome = Attempt
      Counter += 1
    else:
      Counter += 1
  
  return Outcome

