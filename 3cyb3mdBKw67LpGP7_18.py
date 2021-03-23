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
  new_num = ''
  n_str = str(n)
  for i, v in enumerate(n_str):
    if i == 0 and n_str[i+1] != v:
      new_num += v * 3
    elif i == len(n_str) - 1 and n_str[i - 1] != v:
      new_num += v * 3
    elif n_str[i-1] != v and n_str[i+1] != v:
      new_num += v * 3
    else:
      new_num += v
  return int(new_num)

