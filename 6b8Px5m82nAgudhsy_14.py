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
  n = num
  num = list(str(num))
  if sorted(num)[::-1] == num:
    return n
  for i in range(2, len(num) + 1):
    temp = sorted(num[-i:])
    start = ''.join(num[:-i])
    for x in range(len(temp)):
      check = int(start + ''.join([temp[x]] + temp[:x] + temp[x + 1:]))
      if check > n:
        return check

