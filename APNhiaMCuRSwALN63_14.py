"""


A string is an **almost-palindrome** if, by changing **only one character** ,
you can make it a palindrome. Create a function that returns `True` if a
string is an **almost-palindrome** and `False` otherwise.

### Examples

    almost_palindrome("abcdcbg") ➞ True
    # Transformed to "abcdcba" by changing "g" to "a".
    
    almost_palindrome("abccia") ➞ True
    # Transformed to "abccba" by changing "i" to "b".
    
    almost_palindrome("abcdaaa") ➞ False
    # Can't be transformed to a palindrome in exactly 1 turn.
    
    almost_palindrome("1234312") ➞ False

### Notes

Return `False` if the string is already a palindrome.

"""

def almost_palindrome(txt):
    arr = txt[:len(txt) // 2]
    arr2 = txt[len(txt) // 2:]
    if len(arr2) > len(arr):
        arr2 = arr2[1:]
    if arr2[0] == arr[-1]:
        arr2 = arr2[::-1]
    minimum = [set(arr), set(arr2)]
    minimum.sort(key=len)
    if len(set(arr)) == len(set(arr2)) == 1:
        return False
    return len(set(arr + arr2)) == len(minimum[0]) + 1

