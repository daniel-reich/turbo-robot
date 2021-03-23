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
  new_word = ""
  
  for ch in word:
    if ch == 'Z':
      ch = 'A'
    elif ch == 'z':
      ch = 'a'
    else:
      ch = chr(ord(ch) + 1)
      
    new_word += ch
      
  return new_word;

