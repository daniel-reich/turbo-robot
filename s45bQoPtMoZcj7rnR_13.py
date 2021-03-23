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

def closest_palindrome(num):
    i = 0
    while True:
        first_candidate, second_candidate = num - i, num + i
        if str(first_candidate) == str(first_candidate)[::-1]:
            return first_candidate
        elif str(second_candidate) == str(second_candidate)[::-1]:
            return second_candidate
        else:
            i += 1

