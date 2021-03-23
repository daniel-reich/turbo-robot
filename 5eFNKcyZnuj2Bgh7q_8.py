"""


A number `n` is automorphic if `n^2` ends in `n`.

For example: n=5, n^2=2 **5**

Create a function that takes a number and returns `True` if the number is
automorphic, `False` if it isn't.

### Examples

    is_automorphic(5) ➞ True
    
    is_automorphic(8) ➞ False
    
    is_automorphic(76) ➞ True

### Notes

N/A

"""

def is_automorphic(n):
  return str(int(n)**2)[-(len(str(n))):] == str(n)

