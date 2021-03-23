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
    idx1, idx2 = 0, 1 
​
    while idx2 < len(words):
        w1 = words[idx1]
        w2 = words[idx2]
​
        if abs(len(w1) - len(w2)) > 1:
            return False
        
        if abs(len(w1) - len(w2)) == 0:
            sameCount = 0
            i = 0
            while i < len(w1):
                if w1[i] == w2[i]:
                    sameCount += 1
                i += 1
            if len(w1) - sameCount > 1:
                return False
        
        elif abs(len(w1) - len(w2)) == 1:
            found = False
            i = 0
            
            if len(w1) < len(w2):
                while i < len(w2):
                    wordCheck = ''
                    j = 0
                    while j < len(w2):
                        if j != i:
                            wordCheck += w2[j]
                        j += 1
​
                    if wordCheck == w1:
                        found = True
                        break
                    i += 1
                
                if found == False:
                    return False
            
            else:
                while i < len(w1):
                    wordCheck = ''
                    j = 0
                    while j < len(w1):
                        if j != i:
                            wordCheck += w1[j]
                        j += 1
                    
                    if wordCheck == w2:
                        found = True
                        break
                    i += 1
                
                if found == False:
                    return False
​
        idx1 += 1
        idx2 += 1
​
    return True

