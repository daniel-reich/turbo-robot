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

def move(str):
    s=""
    for i in str:
        s+=chr(ord(i)+1)
    return s

