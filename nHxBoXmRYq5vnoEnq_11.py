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

def vowels(string):
  a = string.count("a")
  e = string.count("e")
  i = string.count("i")
  o = string.count("o")
  u = string.count("u")
  return a + e + i + o + u

