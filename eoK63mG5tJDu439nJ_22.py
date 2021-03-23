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
    t=0
 
    def distance(a, b):
        costs = []
        for j in range(len(b) + 1):
            costs.append(j)
        for i in range(1, len(a) + 1):
            costs[0] = i
            nw = i - 1
            for j in range(1, len(b) + 1):
                cj = min(1 + min(costs[j], costs[j - 1]),
                       nw if a[i - 1] == b[j - 1] else nw + 1)
                nw = costs[j]
                costs[j] = cj
 
        return costs[len(b)]
 
    for i in range(0,len(words)-1):
        if distance(words[i],words[i+1])==1:
            t=t+0
        else:
            t=t+1
    if t==0:
        return True
    else:
        return False

