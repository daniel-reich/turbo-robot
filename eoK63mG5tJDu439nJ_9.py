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
def levenshtein(seq1, seq2):
    a=[]
    x = len(seq1) + 1
    y = len(seq2) + 1
    m= np.zeros ((x,y))
    for x in range(x):
        m[x, 0] = x
    for y in range(y):
        m[0, y] = y
    z=[]    
    for x in range(0,x):
        for y in range(0,y):
            if seq1[x-1] == seq2[y-1]:
                m[x,y] = min(m[x-1, y] + 1, m[x-1, y-1],m[x, y-1] + 1)                
            else:
                m[x,y] = min(m[x-1,y] + 1,m[x-1,y-1] + 1,m[x,y-1] + 1) 
        a.append(int(m[x - 1,y - 1]))
    return a
def isWordChain(words):
    for word in range(len(words)-1):
        x=[]
        seq1=words[word]
        seq2=words[word+1]
        x.append((levenshtein(seq1,seq2))) 
    print(x) 
    if x[0][2]!=1or x[0][-1]==1:
        return True
    else:
        return False

