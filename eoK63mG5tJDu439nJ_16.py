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
  for i in range(1,len(words)):
    if len(words[i-1])==len(words[i]) and sum(a!=b for a,b in zip(words[i-1],words[i]))==1:
      continue
    elif len(words[i])-len(words[i-1])==1:
      for c in words[i-1]:
        if c not in words[i]:
          return False
        else:
          continue
    elif len(words[i-1])-len(words[i])==1:
      for c in words[i]:
        if c not in words[i-1]:
          return False
        else:
          continue
    else:
      return False
  return True

