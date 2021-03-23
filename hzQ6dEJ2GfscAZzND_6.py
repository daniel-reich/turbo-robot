"""


Create a function that takes a number as its parameter and returns another
function.The returned function must take a list of numbers as its parameter,
and return a list of the numbers divided by the number that was passed into
the first function.

### Examples

    first = factory(15)
    // returns a function first.
    
    lst = [30, 45, 60]
    // 30 / 15 = 2, 45 / 15 = 3, 60 / 15 = 4
    
    first(lst) ➞ [2, 3, 4]
    second = factory(2)
    // returns a function second.
    
    lst = [2, 4, 6]
    // 2 / 2 = 1, 4 / 2 = 2, 6 / 2 = 3
    
    second(lst) ➞ [1, 2, 3]

### Notes

Rounding not required.

"""

def factory(n):
  def divide_by_15(lst):
    return [i/n for i in lst]
  return divide_by_15

