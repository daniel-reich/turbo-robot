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

def slicer(s,t):
  A=[s.find(x) for x in t]
  if len(A)==1:
    return '[{}]'.format(A[0])
  else:
    d=A[1]-A[0]
    if d==1:
      if A[0]==0:
        if A[-1]==len(s)-1:
          return '[:]'
        else:
          return '[:{}]'.format(A[-1]+1)
      else:
        if A[-1]==len(s)-1:
          return '[{}:]'.format(A[0])
        else:
          return '[{}:{}]'.format(A[0], A[-1]+1)
    else:
      if d>1:
        if A[0]==0 or A[0]==len(s)-1:
          if A[-1]==len(s)-1 or A[-1]-d<0 or A[-1]+d>=len(s):
            return '[::{}]'.format(d)
          else:
            return '[:{}:{}]'.format(A[-1]+1, d)
        else:
          if A[-1]==len(s)-1 or A[-1]-d<0 or A[-1]+d>=len(s):
            return '[{}::{}]'.format(A[0],d)
          else:
            return '[{}:{}:{}]'.format(A[0], A[-1]+1, d)
      else:
        if A[0]==0 or A[0]==len(s)-1:
          if A[-1]==len(s)-1 or A[-1]+d<0 or A[-1]-d>=len(s):
            return '[::{}]'.format(d)
          else:
            return '[:{}:{}]'.format(A[-1]-1, d)
        else:
          if A[-1]==len(s)-1 or A[-1]+d<0 or A[-1]-d>=len(s):
            return '[{}::{}]'.format(A[0],d)
          else:
            return '[{}:{}:{}]'.format(A[0], A[-1]-1, d)

