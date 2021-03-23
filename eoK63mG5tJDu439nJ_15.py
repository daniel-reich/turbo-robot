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
  return all(isok(words[i],words[i+1]) for i in range(len(words)-1))
​
def isok(w1, w2):
  # ww is list of variation on word (1 letter missing)
  ww1 = [w1[:x] + w1[x+1:] for x in range(len(w1))]
  ww2 = [w2[:x] + w2[x+1:] for x in range(len(w2))]
  c1 = any(True for x in ww2 if x in ww1) # condition change letter
  c2 = any(True for x in ww2 if w1 == x) # condition add letter
  c3 = any(True for x in ww1 if w2 == x) # condition substract letter
  return any([c1, c2, c3])

