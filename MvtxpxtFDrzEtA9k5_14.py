"""


A number may not be a palindrome, but its descendant can be. A number's direct
child is created by summing each pair of adjacent digits to create the digits
of the next number.

For instance, `123312` is not a palindrome, but its next child `363` is,
where: `3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2`.

Create a function that returns `True` if the **number itself** is a palindrome
or any of its **descendants down to 2 digits** (a 1-digit number is trivially
a palindrome).

### Examples

    palindrome_descendant(11211230) ➞ True
    # 11211230 ➞ 2333 ➞ 56 ➞ 11
    
    palindrome_descendant(13001120) ➞ True
    # 13001120 ➞ 4022 ➞ 44
    
    palindrome_descendant(23336014) ➞ True
    # 23336014 ➞ 5665
    
    palindrome_descendant(11) ➞ True
    # Number itself is a palindrome

### Notes

Numbers will always have an even number of digits.

"""

from collections import deque
​
​
def palindrome_descendant(num):
    if check_palindrome(str(num)):
        return True
    else:
        num_desc_1 = add_digits(num)
        if len(str(num_desc_1)) >= 2:
            if check_palindrome(str(num_desc_1)):
                return True
            else:
                num_desc_2 = add_digits(num_desc_1)
                if len(str(num_desc_2)) >= 2:
                    return check_palindrome(str(num_desc_2))
                else:
                    return False
        else:
            return False
​
​
def check_palindrome(a_str):
    if len(a_str) % 2 == 0:
        if a_str[:int(len(a_str) / 2)] == a_str[-1:int(len(a_str) / 2 - 1):-1]:
            return True
        else:
            return False
    elif a_str[:int(len(a_str) / 2)] == a_str[-1:int(len(a_str) / 2):-1]:
            return True
    else:
        return False
​
​
def add_digits(num):
    num_str = deque(str(num))
    new_str = []
    while len(num_str) > 1:
        new_str.append(str(int(num_str.popleft()) + int(num_str.popleft())))
    if len(num_str) == 1:
        new_str.append(num_str.pop())
    return int("".join(new_str))

