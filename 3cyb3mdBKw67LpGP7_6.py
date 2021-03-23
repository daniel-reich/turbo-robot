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
    ans = ""
    n = str(n)
    last = n[0]
    for c in n[1:]:
        if c == last[-1]:
            last += c
        else:
            ans += last if len(last) > 1 else last * 3
            last = c
    ans += last if len(last) > 1 else last * 3
    return int(ans)

