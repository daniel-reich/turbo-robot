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
    temp = ''
    for i in range(len(n)-1):
        if n[i] != n[i+1]:
            temp += n[i]+','
        else:
            temp += n[i]
    temp += n[i+1]
    temp = temp.split(',')
​
    for i in range(len(temp)):
        if len(temp[i]) == 1:
            temp[i] = temp[i]*3
​
​
    return int(''.join(temp))

