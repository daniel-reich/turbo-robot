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
​
    lst_1 = list(str(n))
    lst_2, lst_3 = [], []
​
    for i in range(len(lst_1) - 1):
        if lst_1[i] != lst_1[i+1]:
            lst_2.append(lst_1[i])
            lst_2.append(',')
        else:
            lst_2.append(lst_1[i])
    lst_2.append(lst_1[-1])
​
    lst_2 = ''.join(lst_2).split(',')
​
    for i in lst_2:
        if len(i) == 1:
            lst_3.append(i * 3)
        else:
            lst_3.append(i)
​
    return int(''.join(lst_3))

