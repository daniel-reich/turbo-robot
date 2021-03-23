"""


Create a function that determines whether it is possible to build a palindrome
from the characters in a string.

### Examples

    possible_palindrome("acabbaa") ➞ True
    # Can make the following palindrome: "aabcbaa"
    
    possible_palindrome("aacbdbc") ➞ True
    # Can make the following palindrome: "abcdcba"
    
    possible_palindrome("aacbdb") ➞ False
    
    possible_palindrome("abacbb") ➞ False

### Notes

N/A

"""

def possible_palindrome(txt):
    is_palindrome = True
    lst = [x for x in txt]
    lst.sort()
    st = list(set(lst))
    
    counted = list()
    for el in st:
        counted.append(lst.count(el))
    
    remainder = [x%2 for x in counted]
    sumr = sum(remainder)
        
    if len(txt)%2 == 1: #odd len
        #print("txt is odd length")                       
        if sumr > 1:
            is_palindrome = False
        
    else: #even length
        #print("txt is even length")                        
        if sumr > 0:
            is_palindrome = False
    
    return is_palindrome

