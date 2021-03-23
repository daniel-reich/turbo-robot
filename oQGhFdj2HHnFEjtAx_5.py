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
  if string==slic:
    return "[:]"
  for x in range(len(string)):
    if string[x]==slic:
      return "["+str(x)+"]"
    for y in range(len(string)):
      if string[:y]==slic:
        return "[:"+str(y)+"]"
      if string[x:y]==slic:
        return "["+str(x)+":"+str(y)+"]"
      for z in range(-len(string),len(string)):
        if z!=0:
          if string[::z]==slic:
            return "[::"+str(z)+"]"
          elif string[x::z]==slic:
            return "["+str(x)+"::"+str(z)+"]"
          elif string[:y:z]==slic:
            return "[:"+str(y)+":"+str(z)+"]"
          elif string[x:y:z]==slic:
            return "["+str(x)+":"+str(y)+":"+str(z)+"]"

