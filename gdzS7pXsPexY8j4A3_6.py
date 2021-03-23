"""


Create a function that takes in a list of integers and returns the number of
even or odd digits for each number, depending on the parameter.

### Examples

    count_digits([22, 53, 99, 61, 777, 8], "odd") ➞ [0, 2, 2, 1, 3, 0]
    
    count_digits([22, 53, 99, 61, 777, 8], "even") ➞ [2, 0, 0, 1, 0, 1]
    
    count_digits([54, 113, 89, 10], "odd") ➞ [1, 3, 1, 1]
    
    count_digits([54, 113, 89, 10], "even") ➞ [1, 0, 1, 1]

### Notes

N/A

"""

def odd(n):
  n = str(n)
  x = sum(1 for i in n if int(i) % 2)
  return x
​
def even(n):
  n = str(n)
  x = sum(1 for i in n if not int(i) % 2)
  return x
​
def count_digits(lst, key):
​
  if key == 'odd':
    l = [odd(i) for i in lst]
  if key == 'even':
    l = [even(i) for i in lst]
​
  return l

