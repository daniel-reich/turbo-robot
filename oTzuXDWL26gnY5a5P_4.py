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
  if num<2:
    return 0
  else:
    c=2
    ans=0
    while True:
      m = 0
      for x in range(c//2,1,-1):
        if c%x==0:
          m=1
          break
      if not m:
        ans+=1
      if c<num:
        c+=1
      else:
        break
    return ans

