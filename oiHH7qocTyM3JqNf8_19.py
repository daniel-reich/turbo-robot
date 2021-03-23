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

from string import ascii_letters
​
def move(ex):
    lst_ex = []
​
    for letter in ex:
        if letter in ascii_letters:
            lst_ex.append(ascii_letters[(ascii_letters.index(letter) + 1)])
​
    new_ex = "".join(lst_ex)
​
    return new_ex

