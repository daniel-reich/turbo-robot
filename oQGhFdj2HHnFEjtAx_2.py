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

def slicer(s, q, z=True, x=False):
    p, w, t = [s.find(i) for i in q], "[", len(s) - z
    if len(p) == z: return str(p)
    j, f, a = p[z] - p[x], p[x], p[-z]; d = z if j > x else -z
    w += str(f) if f != x and f != t else ""
    w += (":" + str(a + d)) if x <= a + j <= t else ":"
    return w+((":" + str(j)) if j != z else "") + "]"

