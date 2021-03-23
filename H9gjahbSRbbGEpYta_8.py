"""


Create a function that takes two numbers `n1` `n2` and multiplies them
**without using** `*`.

### Examples

    multiply(3, 2) ➞ 6
    
    multiply(4, 10) ➞ 40
    
    multiply(-2, 4) ➞ -8

### Notes

Do not use `*` for this challenge.

"""

def multiply(n1, n2):
  pos = n1 > 0 and n2 > 0 or n1 < 0 and n2 < 0
  n1, n2 = abs(n1), abs(n2)
  count = 1
  answer = n1
  while count < n2:
    answer += n1
    count += 1
  if pos == False:
    return -answer
  return answer

