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
    print(words)
    prev = None
    for x in words:
        print(x)
        pointer = x
        spent = False
​
        if prev:
            if prev == pointer: return False
​
            if len(prev) == len(pointer):
                for i, l in enumerate(prev):
                    if pointer[i] != l and not spent:
                        spent = True
                    elif pointer[i] != l and spent:
                        return False
            else:      
            # did you add or subtract
                if len(prev) < len(pointer):
                    w, a = pointer, prev
                if len(prev) > len(pointer):
                    w, a = prev, pointer
​
                for b in a:
                    if b not in w:
                        return False
​
                if len(w) - len(a) != 1: return False
​
​
​
        prev = pointer
    return True

