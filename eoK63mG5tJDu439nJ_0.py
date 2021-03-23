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

def isWordChain(words):
    for x, y in zip(words, words[1:]):
        if len(x) == len(y) and sum(1 for i in x if i not in y) == 1:
            continue
        elif len(x) + 1 == len(y) and sum(1 for i in x if i not in y) == 0:
            continue
        elif len(y) + 1 == len(x) and sum(1 for i in y if i not in x) == 0:
            continue
        else:
            return False
    return True

