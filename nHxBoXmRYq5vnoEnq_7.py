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

def vowels(string, c=0):
  if not string: return c
  if string[0] in 'aeiou': c += 1
  return vowels(string[1:], c)
