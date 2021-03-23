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

import difflib
def isWordChain(words):
    def check(a, b):
        diff = list(difflib.ndiff(a,b))
        return sum('+' in d for d in diff) <= 1 and sum('-' in d for d in diff) <= 1
    return all(check(words[i], words[i+1]) for i in range(len(words)-1))

