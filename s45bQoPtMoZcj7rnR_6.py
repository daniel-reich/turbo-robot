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

def closest_palindrome(n):
 a=n
 while str(a)!=str(a)[::-1]:a-=1
 b=n
 while str(b)!=str(b)[::-1]:b+=1
 return min(a,b,key=lambda x:abs(n-x))

