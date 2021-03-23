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
    # simple cases:
    if slic == string:
        return "[:]"
    if slic == string[::-1]:
        return "[::-1]"
    if slic == string[0]:
        return "[0]"
    n = len(slic)
    m = len(string)
    if slic == string[:n]:
        return "[:" + str(n) + "]"
    if slic == string[-n:]:
        return "[-" + str(n) + ":]"
    if slic in string:
        idx = string.find(slic)
        return "[" + str(idx) + ":" + str(idx + n) + "]"
    # "forward" cases:
    for start in range(m - 1):
        delta = 2
        while True:
            if start + delta * (n - 1) >= m:
                break
            s_slice = ''.join([string[start+k*delta] for k in range(n)])
            if s_slice == slic:
                ans = "["
                if start > 0 :
                    ans += str(start)
                ans += ":"
                end = start + delta * (n - 1)
                if end + delta < m:
                    ans += str(end + 1) 
                ans += ":" + str(delta) + "]"
                return ans
            delta += 1
    # "reverse" cases:
    for start in range(m - 1, 0, -1):
        delta = -1
        while True:
            if start + delta * (n - 1) < 0:
                break
            s_slice = ''.join([string[start+k*delta] for k in range(n)])
            if s_slice == slic:
                ans = "[" 
                if start < m - 1:
                    ans += str(start)
                ans += ":"
                end = start + delta * n
                if end >= 0:
                    ans += str(end)
                ans += ":" + str(delta) + "]"
                return ans
            delta -= 1

