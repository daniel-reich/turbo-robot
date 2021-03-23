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

def difference_by_one(words):
  def difference():
    return abs(len(words[0]) - len(words[1]))
  if difference() > 1:
    return False
  elif difference() == 1:
    words.sort(key = lambda x: len(x))
    if words[0]== words[1][:-1]:
      return True
    elif words[0] == words[1][1::]:
      return True
    else:
      for i in range(0,len(words[1])):
        if words[0][i] != words[1][i]:
          return words[0] == words[1][:i] + words[1][i+1::]         
  else:
    diff = 0
    for i in range(0,len(words[0])):
      if words[0][i] != words[1][i]:
        if diff == 0:
          diff += 1
        else:
          return False
    return True
        
      
def isWordChain(words):
  for i in range(0,len(words)-1):
    if difference_by_one([words[i],words[i+1]]) == False:
      return False
  return True

