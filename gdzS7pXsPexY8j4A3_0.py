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

def count_digits(lst, t):
  chars = '13579' if t == 'odd' else '02468'
  return [sum(i in chars for i in str(num)) for num in lst]

