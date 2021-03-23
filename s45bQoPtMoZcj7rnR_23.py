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

def check_palindrome(ans, num):
    l = num - (abs(num - ans))
    if str(l) == str(l)[::-1]:
        return l
    else:
        return ans
​
def closest_palindrome(num):
    s = str(num)
    if len(s) % 2 == 0:
        mid = (s[0:len(s) // 2])
        ans = int(mid + mid[::-1])
    else:
        mid = (s[0:len(s) // 2 + 1])
        ans = int(mid + mid[::-1][1:])
    return check_palindrome(ans, num)

