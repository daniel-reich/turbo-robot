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
  
  class Number:
  
    def __init__(self, val):
      self.v = val
      self.d = [int(i) for i in str(val)]
    
    def return_type(self, t):
      odd = []
      even = []
      for digit in self.d:
        if digit % 2 != 0:
          odd.append(digit)
        else:
          even.append(digit)
      return len(eval(t))
  
  numbers = []
  
  for number in lst:
    numbers.append(Number(number))
  
  count = []
  
  for number in numbers:
    count.append(number.return_type(t))
  
  return count

