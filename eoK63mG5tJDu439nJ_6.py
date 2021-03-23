"""


Let's update our previous **word-chain** definition. In this 2.0 version, a
**word-chain** is an array of words, where the next word is formed by either:

  1. Changing exactly **one** letter from the previous word
  2. Adding or subtracting **one** letter

Note: You can only do one (not both) for each word change.

### Examples

    isWordChain(["row", "crow", "crown", "brown", "brawn"]) ➞ True
    # add "c" to "row" to get "crow", "n" to get "crown", etc. 
    
    isWordChain(["flew", "flaw", "flan", "flat", "fat", "rat", "rot", "tot"]) ➞ True
    
    isWordChain(["meek", "meet", "meat", "teal"]) ➞ False
    # "meat" => "teal" changes 2 letters (can only change 1)
    
    isWordChain(["run", "runny", "bunny"]) ➞ False
    # "run" => "runny" adds 2 letters (can only add 1)

### Notes

  * All words will be in lower-case.

"""

import numpy as np
​
def isWordChain(words):
    last = np.array([ord(c) for c in words[0]])
    for i in range(1,len(words)):
        current = np.array([ord(c) for c in words[i]])
        if abs(len(current)-len(last))>1: return False
        elif abs(len(current)-len(last)) == 0:
            xor_0 = (last-current != 0)
            if np.sum(xor_0) > 1: return False
        else:
            longer = current if len(current)>len(last) else last
            shorter = last if len(current)>len(last) else current
            xor_start = (longer[:-1]-shorter == 0)
            xor_end = (longer[1:]-shorter == 0)
            xor = np.logical_or(xor_start, xor_end)
            if np.sum(xor) != len(xor): return False
        last = current
    return True

