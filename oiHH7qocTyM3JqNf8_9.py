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
  import string
  alph = [i for i in string.ascii_lowercase]
  lst = []
  for letter in word:
    nxt_i = alph.index(letter)+1
    lst.append(alph[nxt_i])
  return "".join(lst)

