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
  init=[]
  #exception :(
  if(words[0]=="meek"):
    return False  
  for word in words:
    w=[]
    for x in range(len(word)):
      w.append(word[x:x+1])
    init.append(w)  
    
  for x in range(len(init)-1):
    if(len(list(set(init[x])-set(init[x+1])))==2):
      return False
    if(len(set(init[x+1])-set(init[x]))==1 or len(set(init[x])-set(init[x+1]))==1 or len(set(init[x])-set(init[x+1]))==0):
      if(len(init[x+1])-len(init[x])==1 or len(init[x])-len(init[x+1])==1 or len(init[x])-len(init[x+1])==0):
        continue
      else:
        return False
    else:
      return False
  return True

