"""


Given a number, insert duplicate digits on both sides of all digits which
appear in a group of 1.

### Worked Example

    numbers_need_friends_too(22733) ➞ 2277733
    
    # The number can be split into groups 22, 7, and 33.
    # 7 appears on its own.
    # Put 7s on both sides to create 777.
    # Put the numbers together and return the result.

### Examples

    numbers_need_friends_too(123) ➞ 111222333
    
    numbers_need_friends_too(56657) ➞ 55566555777
    
    numbers_need_friends_too(33) ➞ 33

### Notes

All tests will include positive integers.

"""

def numbers_need_friends_too(n):
  t,s,l="",str(n),len(str(n))
  for i,x in enumerate(s):
    if (not i and s[i+1]!=x) or (i==l-1 and s[i-1]!=x) or (0<i<l-1 and x not in s[i-1:i+2:2]):
      t+=x*3
    else:
      t+=x
  return int(t)

