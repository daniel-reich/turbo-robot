"""


Given a **two digit** number, return `True` if that number contains **one
even** and **one odd** digit.

### Examples

    one_odd_one_even(12) ➞ True
    
    one_odd_one_even(55) ➞ False
    
    one_odd_one_even(22) ➞ False

### Notes

N/A

"""

def one_odd_one_even(n):
  nums = list(map(int, str(n)))
  counter = [0,0]
  for n in nums:
    if n % 2 == 0:
      counter[0] = 1
    elif n % 2 != 0:
      counter[1]= 1
  return counter == [1,1]

