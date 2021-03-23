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

def canChain(w1, w2):
    l1, l2 = len(w1), len(w2)
    if abs(l1 - l2) > 1:
        return False
    if l1 == l2:
        return sum(1 if w1[i] != w2[i] else 0 for i in range(l1)) == 1
    if l2 > l1:
        return sum(1 if w2[i] not in w1 else 0 for i in range(l2)) <= 1
    return sum(1 if w1[i] not in w2 else 0 for i in range(l1)) <= 1
​
def isWordChain(words):
    return all(canChain(w1, w2) for w1, w2 in zip(words, words[1:]))

