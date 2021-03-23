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
    ind  = [string.index(x) for x in slic]
    if len(ind) == 1: return  str(ind)
    diff =  ind[-1] - ind[-2]
    start = '' if not ind[0] or ind[0]+1 == len(string) else str(ind[0])
    step = '' if diff == 1 else str(diff)
    if not ind[-1] or ind[-1]+diff >= len(string) or ind[-1] + diff < 0:
        end = '' 
    else:
        diff = 1 if diff >= 1 else -1
        end = str(ind[-1]+diff) 
    return '[{}:{}]'.format(start, end) if not step else '[{}:{}:{}]'.format(start, end, step)

