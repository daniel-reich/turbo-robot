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

def digits(number):
  
  n_digits = 0
  so_far = 1
  length = 0
​
  while True:
    if so_far >= number:
      n_digits += length * (number - int(so_far/10))
      break
    else:
      n_digits += length * (so_far - int(so_far/10))
      length += 1
      so_far = so_far * 10
  
  return n_digits

