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
  n = [int(i) for i in str(num)]
  for i in range (2,len(n)+1):
    if n[-i] < n[1-i]:
      tail = n[-i:].copy()
      tail.sort()
      digit = 0
      for j in tail:
        if j > n[-i] and (digit==0 or j < digit):
          digit = j
      n[-i] = digit
      tail.remove(digit)
      n[1-i:] = tail
      break
  num = ""
  for i in n:
    num += str(i)
  return int(num)

