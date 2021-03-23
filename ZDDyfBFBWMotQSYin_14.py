"""


A number `n` is a Harshad (also called Niven) number if it is divisible by the
sum of its digits. For example, 666 is divisible by 6 + 6 + 6, so it is a
Harshad number.

Write a function to determine whether the given number is a Harshad number.

### Examples

    is_harshad(209) ➞ True
    
    is_harshad(41) ➞ False
    
    is_harshad(12255) ➞ True

### Notes

N/A

"""

def is_harshad(num):
  total = [int(str(num)[i]) for i in range(len(str(num)))]
  total = sum(total)
  if total == 0:
    return False
  if num % total == 0:
    return True
  else:
    return False

