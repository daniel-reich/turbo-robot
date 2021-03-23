"""


A **pandigital** number contains all digits (0-9) at least once. Write a
function that takes an integer, returning `True` if the integer is pandigital,
and `False` otherwise.

### Examples

    is_pandigital(98140723568910) ➞ True
    
    is_pandigital(90864523148909) ➞ False
    # 7 is missing.
    
    is_pandigital(112233445566778899) ➞ False

### Notes

Think about the properties of a pandigital number when all duplicates are
removed.

"""

def is_pandigital(n):
  holder = []
  for num in str(n):
    holder.append(num)
​
  unique = list(map(int, list(dict.fromkeys(holder))))
  values_to_check = list(range(0, 10))
​
  result = all(elem in unique for elem in values_to_check)
  return(result)

