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
  if num <= 1:
    return 0
  
  else:
    count = 1
    for i in range(3,num):
      l = []
      for j in range(2,i):
        l.append(i%j)
      if l.count(0) == 0:
        count += 1
    return count

