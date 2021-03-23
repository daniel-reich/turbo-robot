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

from collections import Counter
def possible_palindrome(txt):
    counter = Counter(txt)
    values = counter.values()
    total_letters = sum(values)
    odd_total = sum(i for i in values if i%2 != 0)
    even_total = sum(i for i in values if i%2 == 0)
    if (odd_total%2 != 0 and total_letters - odd_total >= 2)\
    or (total_letters in (odd_total,even_total) \
    and total_letters > len(counter.keys())):
        return True
    else:
        return False

