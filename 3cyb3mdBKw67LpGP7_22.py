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
  n = str(n)
  a,z = n[0]*[3,1][n[1]==n[0]],n[-1]*[3,1][n[-2]==n[-1]]
  lst = [v*[3,1][v in [n[i-1],n[i+1]]] for i,v in enumerate(n[1:-1],1)]
  return int(a+''.join(lst)+z)

