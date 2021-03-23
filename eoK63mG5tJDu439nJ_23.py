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
  for i in range(len(words)-1):
    if len(words[i]) == len(words[i+1]):
      diff  = 0
      for j in range(len(words[i])):
        if words[i][j] != words[i+1][j]: diff += 1
      if diff != 1: return False
    if len(words[i]) < len(words[i+1]):
      if len(words[i])+1 == len(words[i+1]) and words[i] in words[i+1]:
        continue
      elif len(words[i])+1 != len(words[i+1]): return False
      else:
        diff = 0
        for j in range(len(words[i+1])):
          if words[i][j-diff] != words[i+1][j]:
            diff += 1
        if diff != 1: return False
    if len(words[i]) > len(words[i+1]):
      if len(words[i])-1 == len(words[i+1]) and words[i+1] in words[i]:
        continue
      elif len(words[i])-1 != len(words[i+1]): return False
      else:
        diff = 0
        for j in range(len(words[i])):
          if words[i][j] != words[i+1][j-diff]:
            diff += 1
        if diff != 1: return False
  return True

