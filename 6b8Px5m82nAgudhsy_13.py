"""


Write a function that returns the next number that can be created from the
same digits as the input.

### Examples

    next_number(19) ➞ 91
    
    next_number(3542) ➞ 4235
    
    next_number(5432) ➞ 5432
    
    next_number(58943) ➞ 59348

### Notes

  * If no larger number can be formed, return the number itself.
  *  **Bonus** : See if you can do this without generating all digit permutations.

"""

def next_number(num):
  digits = [int(c) for c in str(num)]
  result = next_number_r([], sorted(digits), digits)
  if result:
    return int(''.join([str(d) for d in result]))
  return num
def next_number_r(current, digits, minimum):
  if len(current) == len(minimum):
    return False
  for d in digits:
    if d < minimum[len(current)]:
      continue
    if d > minimum[len(current)]:
      next_digits = digits[:]
      next_digits.remove(d)
      if current + [d] + list(next_digits) != minimum:
        return current + [d] + list(next_digits)
      continue
    next = current + [d]
    next_digits = digits[:]
    next_digits.remove(d)
    result = next_number_r(current + [d], next_digits, minimum)
    if result:
      return result
  return False

