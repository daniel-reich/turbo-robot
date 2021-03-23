"""


Imagine you took all the numbers between 0 and `n` and concatenated them
together into a long string. How many digits are there between 0 and `n`?
Write a function that can calculate this.

There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and
there are 189 digits between 0 and 100.

### Examples

    digits(1) ➞ 0
    
    digits(10) ➞ 9
    
    digits(100) ➞ 189
    
    digits(2020) ➞ 6969

### Notes

The numbers are going to be rather big so creating that string won't be
practical.

"""

def dlen(num):
  return len(str(num))
​
def decrease_to_next_digit(number):
  num_digits = dlen(number)
  next_num_str = (num_digits-1)*"9"
  if next_num_str == "":
    return 0
  return int(next_num_str)
​
def digits(number):
  number = number-1
  total = 0
  while number > 0:
    num_digits = dlen(number)
    next_number = decrease_to_next_digit(number)
    diff = number - next_number
    total += diff*num_digits
    number = next_number
  return total

