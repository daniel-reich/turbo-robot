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
  
  new_n = ''
  prev_indexes = []
  
  for index in range(len(str(n))):
    if index in prev_indexes:
      continue
    digit = str(n)[index]
    try:
      next_digit = str(n)[index + 1]
    except IndexError:
      next_digit = ''
  # print(digit, next_digit)
    if next_digit != digit:
      new_n += digit * 3
    else:
      new_n += digit
      ni = index + 1
      try:
        while str(n)[ni] == digit:
          prev_indexes.append(ni)
          ni += 1
          new_n += digit
      except IndexError:
        continue
  
  return int(new_n)

