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
  letters="abcdefghijklmnopqrstuvwxyz"
  new_word=""
  for x in word:
    i=letters.find(x)
    new_word+=letters[i+1]
  return new_word

