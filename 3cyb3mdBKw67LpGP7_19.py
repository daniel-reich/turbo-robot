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
    i, j, size = 0, 1, len(n)
    new_n = ''
​
    while i < size:
        while j < size and n[i] == n[j]:
            j += 1
        if j - i > 1:
            new_n += n[i:j]
        else:
            new_n += n[i]*3  # lonely number
        i = j
        j += 1
​
    return int(new_n)

