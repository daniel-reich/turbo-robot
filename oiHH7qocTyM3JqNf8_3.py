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

alphabet = "abcdefghijklmnopqrstuvwxyz"
def move(word):
  string = ""
  for char in word:
    i = alphabet.index(char)
    string += alphabet[i + 1]
  return string

