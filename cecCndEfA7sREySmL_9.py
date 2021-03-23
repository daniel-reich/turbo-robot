"""


This challenge has five miniature exercises to help practice proficiency in
string slicing. Check the examples below for a visual indicator of how to
slice the strings. Good luck!

### Examples

    txt = "abcdefghijklmnopqrstuvwxyz"
    challenge1(txt) ➞ "abcde"
    # First 5 characters of the string.
    
    challenge2(txt) ➞ "vwxyz"
    # Last 5 characters of the string.
    
    challenge3(txt) ➞ "zyxwvutsrqponmlkjihgfedcba"
    # All characters in the string from back.
    
    challenge4(txt) ➞ "fedcba"
    # First 6 characters in the string (start with 6th character).
    
    challenge5(txt) ➞ "tvxz"
    # Take last 7 characters and only return odd positioned ones.

### Notes

  * Check the **Tests** tab for more examples.
  * See the **Resources** tab for further information on learning string slicing.
  * You are not allowed to concatenate strings together! Results must be achieved purely through string slicing!

"""

txt = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'
​
def challenge1(txt):
  return txt[0:5]
print(challenge1(txt))
  
def challenge2(txt):
  return txt[-5::]
print(challenge2(txt))
​
def challenge3(txt):
    return txt[::-1]
print(challenge3(txt))
  
def challenge4(txt):
  return txt[::-1][-6::]
print(challenge4(txt))
def challenge5(txt):
  return txt[-7::2]
print(challenge5(txt))

