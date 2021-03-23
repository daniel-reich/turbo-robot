"""


Create a function that finds how many prime numbers there are, up to the given
integer.

### Examples

    prime_numbers(10) ➞ 4
    # 2, 3, 5 and 7
    
    prime_numbers(20) ➞ 8
    # 2, 3, 5, 7, 11, 13, 17 and 19
    
    prime_numbers(30) ➞ 10
    # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

### Notes

N/A

"""

def prime_numbers(num):
  if num < 0:
    return 0
  count = 1
  numbers = [i for i in range(3,num+1)]
  for nums in numbers:
    if len([i for i in range(2, nums) if nums % i == 0]) == 0:
      count += 1
  else:
    return count

