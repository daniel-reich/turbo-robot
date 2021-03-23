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
  n=str(n)
  ans=''
  if n[0]!=n[1]:ans+=n[0]*3
  else:ans+=n[0]
  if len(n)>2:
    for i in range(1,len(n)-1):
      if n[i]==n[i-1] or n[i]==n[i+1]:ans+=n[i]
      else:ans+=n[i]*3
  if n[-1]!=n[-2]:ans+=n[-1]*3
  else:ans+=n[-1]
  return int(ans)

