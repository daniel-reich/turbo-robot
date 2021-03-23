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

def slicer(string,slic):
    if len(slic)==1:
        return '['+str(string.find(slic))+']'
    start=string.find(slic[0])
    step=string.find(slic[1])-start
    start=str(start)*(start in range(1,len(string)-1))
    end=string.find(slic[-1])
    if end+step in range(len(string)):
        end=str(end+1-2*(step<0))
    else:
        end=''
    return '['+start+':'+end+(':'+str(step))*(step!=1)+']'

