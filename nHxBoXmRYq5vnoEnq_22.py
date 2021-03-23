"""


Write a function that **recursively** returns the number of vowels in a
string.

 **If it wasn't clear enough already, you should use recursion in your
solution.**

###  Examples

    vowels("apple") ➞ 2
    
    vowels("cheesecake") ➞ 5
    
    vowels("bbb") ➞ 0
    
    vowels("") ➞ 0

### Notes

  * Recursive functions call themselves.
  * All letters will be in lower case.
  * For this challenge, the vowels are a, e, i, o, and u.

"""

def vowels(s):
  if not s:
    return 0
  else:
    return (1 if s[0] in 'aeiou' else 0) + vowels(s[1:])

