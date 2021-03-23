"""


In this challenge you are given a string and a slice made from that string.
Make a function that returns an expression that can be used to make that
slice. Your answer must contain only the minimum number of keystrokes needed
to make the slice.

### Examples

    slicer("abcd", "b") ➞ "[1]"
    
    slicer("abcdefg", "cb") ➞ "[2:0:-1]"
    
    slicer("abcdefg", "be") ➞ "[1::3]"
    
    slicer("abcdefgh", "bdf") ➞ "[1:6:2]"

### Notes

  * Test cases are slices that can be made with the `[start:end:step]` type expression.
  * The strings are composed of unique characters (no repeats).

"""

def slicer(string, slic):
  k = len(string)
  n = string.index(slic[0])
  if len(slic) == 1:
    return "[{}]".format(n)
  m = string.index(slic[-1])
  r = string.index(slic[1]) - n
  if r>1:
    return '[{}:{}:{}]'.format(n if n else '', m+1 if m+r<k else '', r)
  if r==1:
    return '[{}:{}]'.format(n if n else '', m+1 if m+1!=k else '')
  if r<0:
    return '[{}:{}:{}]'.format(n if n!=k-1 else '', m-1 if m+r>=0 else '', r)

