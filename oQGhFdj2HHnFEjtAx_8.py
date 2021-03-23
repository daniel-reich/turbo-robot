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

def slicer(s, slice_part):
  if len(slice_part) == 1 :
    return "[{}]".format(s.index(slice_part))
  indices  = [s.index(e) for e in slice_part]
  step  = [ right  - left for left,right in zip(indices , indices[1:])][0]
  direction  = 1 if step > 0 else -1
  
  display_begin  = "{}".format(indices[0]) if len(s)-1 > indices[0] > 0 else ""
  display_end  = "{}".format(indices[-1]+direction) if len(s) > indices[-1]+step > -1 else ""
  display_step = "{}".format(step) if step != 1 else ""
  display = "{}:{}:{}".format(display_begin , display_end , display_step ).rstrip(":")
  return  "[{}]".format(display if display else ":")

