"""
Create a function that sums the total number of digits between two numbers,
**inclusive**. For example, between the numbers `19` and `22` we have:

    # 19, 20, 21, 22
    (1 + 9) + (2 + 0) + (2 + 1) + (2 + 2) = 19

### Examples

    sum_digits(7, 8) ➞ 15
    
    sum_digits(17, 20) ➞ 29
    
    sum_digits(10, 12) ➞ 6

### Notes

N/A

"""

def sum_digits(a, b):
  new = []
  while a <= b:
   new += [a]
   a += 1
  digits = []
  for x in new:
   while x > 0:
    digits += [x % 10]
    x //= 10
  total = 0
  for x in digits:
   total += x
  return total
​
def sum_digits(a, b):
  return eval('+'.join('+'.join(i for i in str(j)) for j in range(a, b + 1)))

