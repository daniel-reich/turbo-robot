"""


Write a function that returns the closest palindrome number to an integer. If
two palindrome numbers tie in absolute distance, return the **smaller
number**.

### Examples

    closest_palindrome(887) ➞ 888
    
    closest_palindrome(100) ➞ 99
    # 99 and 101 are equally distant, so we return the smaller palindrome.
    
    closest_palindrome(888) ➞ 888
    
    closest_palindrome(27) ➞ 22

### Notes

If the number itself is a palindrome, return that number.

"""

from itertools import count
​
def closest_palindrome(num):
    if str(num) == str(num)[::-1]:
        return num
    for i in count(1):
        if str(num-i) == str(num-i)[::-1]:
            return num-i
        if str(num+i) == str(num+i)[::-1]:
            return num+i

