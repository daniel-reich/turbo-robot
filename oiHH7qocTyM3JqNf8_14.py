"""


Write a function that changes every letter to the next letter:

  * "a" becomes "b"
  * "b" becomes "c"
  * "d" becomes "e"
  * and so on ...

### Examples

    move("hello") ➞ "ifmmp"
    
    move("bye") ➞ "czf"
    
    move("welcome") ➞ "xfmdpnf"

### Notes

There will be no z's in the tests.

"""

def move(word):
  s=""
  for x in word:
    if x.islower():
      if ord(x) < 122:
        s=s+chr(ord(x)+1)
      else:
         s=s+'a'
    else:
      if ord(x) < 90:
        s=s+chr(ord(x)+1)
      else:
         s=s+'A'
  return s

