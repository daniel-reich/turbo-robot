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
  number -= 1
  acc = 0
  if (number < 10):
    return number % 10
  else:
    acc += (number - int("9" * (len(str(number)) - 1))) * len(str(number))
    for i in range(len(str(number)) - 2, 0, -1):
      acc += (int("9" * (i + 1)) - int("9" * i)) * (i + 1)
    return acc + 9

