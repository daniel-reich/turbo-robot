"""


A palindrome is a series of letters or numbers that reads equivocally
backwards. Write a **recursive** function that determines whether a given
string is a **palindrome** or not.

### Examples

    is_palindrome("Go hang a salami, I'm a lasagna hog!") ➞ True
    
    is_palindrome("This phrase, surely, is not a palindrome!") ➞ False
    
    is_palindrome("Eva, can I see bees in a cave?") ➞ True

### Notes

  * Symbols and special characters should be ignored.
  * You are expected to solve this challenge via **recursion**.
  * You can check on the **Resources** tab for more details about _recursion_.

"""

import re
def is_palindrome(p):
    s = re.split('\s|,|!|\?|\'|\.|-', p)
    s = list(filter(None, s))
    normal=[]
    oppos=[]
    for i in s:
        for j in i:
            normal.append(j.lower())
    for i in s[::-1]:
        for j in i[::-1]:
            oppos.append(j.lower())        
    if "".join(normal)=="".join(oppos):
        return True
    else:
        return False

