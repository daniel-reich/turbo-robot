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
    n,l,i = str(n),[], 0
    while i < len(n):
        count = 0
        while 1:
            try:
                if n[i + count] == n[i + count + 1]:
                    count += 1
                else: break
            except IndexError:
                break
        l.append(n[i] * (count + 1))
        if count > 0: i+=count
        i+=1
    return int(''.join([i,i*3][len(i)==1] for i in l))

