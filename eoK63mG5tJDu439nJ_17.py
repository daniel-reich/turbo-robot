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
    for i in range(1, len(words)):
        if abs(len(words[i]) - len(words[i - 1])) > 1:
            return False
        if len(words[i - 1]) == len(words[i]):
            for j in range(len(words[i - 1])):
                if words[i - 1][j] != words[i][j]:
                    if words[i - 1][:j] + words[i - 1][j + 1:] != \
                            words[i][:j] + words[i][j + 1:]:
                        return False
        else:
            if len(words[i - 1]) > len(words[i]):
                bigger, smaller = words[i - 1], words[i]
            else:
                bigger, smaller = words[i], words[i - 1]
            for j in range(len(bigger)):
                if bigger[j] not in smaller:
                    if bigger[:j] + bigger[j + 1:] != smaller:
                        return False
    return True

