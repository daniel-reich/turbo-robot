"""


Create a function that will **recursively** count the number of digits of a
number. Conversion of the number to a string is not allowed, thus, the
approach is recursive.

### Examples

    digits_count(4666) ➞ 4
    
    digits_count(544) ➞ 3
    
    digits_count(121317) ➞ 6
    
    digits_count(0) ➞ 1
    
    digits_count(12345) ➞ 5
    
    digits_count(1289396387328) ➞ 13

### Notes

  * All inputs are integers but some are in exponential form, deal with it accordingly.
  * You are expected to come up with a solution using the concept of **recursion** or the so-called **recursive approach**.
  * Check out the **Resources** for more topics about recursion to read on (if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge or unless otherwise).
  * An **iterative** version of this challenge can be found via this [link](https://edabit.com/challenge/dLYhGnWQ5Q8DRmnbR).

"""

import math
def digits_count(num):
  # your recursive implementation 
  # of the code here
  if abs(num) < 10:
    return 1
  else:
    try:
      lst = list(filter(lambda x: math.ceil(math.log(10,abs(num))) % x == 0, range(2,math.ceil(math.log(10,abs(num))))))
      return lst[0] + digits_count(num // lst[0])
    except IndexError:
      return 1 + digits_count(num // 10)

