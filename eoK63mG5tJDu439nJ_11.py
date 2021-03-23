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

def checkWords(lst):
  lst.sort(key = len)
  w1, w2 = lst[0], lst[1]
  l1, l2 = len(w1), len(w2)
  d = abs(l1-l2)
  if d == 0:
    return sum(1 for i in range(l1) if w1[i] != w2[i]) == 1
  if d == 1:
    return all(i in w2 for i in w1)
  return False
def isWordChain(words):
  return all(checkWords(words[0 + i:2 + i]) for i in range(len(words)-1))

