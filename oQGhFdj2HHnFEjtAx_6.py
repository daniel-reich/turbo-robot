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
    locs = []
    for c in slic:
        locs.append(string.find(c))
​
    length = len(locs)
    lenStr = len(string)
    start = locs[0]
    endA = locs[length - 1]
    end = endA
    inc = 0
    steps = length - 1
    if(steps >= 1):
        inc = (locs[length - 1] - locs[0]) // steps
​
    if(inc > 0):
        end += 1
    elif(inc < 0):
        end -= 1
​
    res = ''
    
    if(length == 1):
        res = '[' + str(start)
    else:
        res = '['
        if(start == 0 or start == (lenStr - 1)):
            res = res + ':'
        else:
            res = res + str(start) + ':'
            
        if((endA + inc) < 0 or (endA + inc) > lenStr - 1):
            res = res
        else:
            res = res + str(end)
​
        if(inc == 1):
            pass
        else:
            res = res + ':' + str(inc)
    res = res + ']'
    
    return res

