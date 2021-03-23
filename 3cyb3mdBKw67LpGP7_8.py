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
    if len(set(str(n))) == 1:
        return n
​
    s = str(n)
    groups = []
    digits = s[0]
​
    for i in s[1:]:
        if i != digits[-1]:
            groups.append(digits)
            digits = ''
        digits += i
​
    if digits == groups[-1]:
        groups[-1] += digits
    else:
        groups.append(digits)
​
    return int(''.join(x * 3 if len(x) == 1 else x for x in groups))

