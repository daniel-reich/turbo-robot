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
  prevword = words[0]
  for i in range(1,len(words)):
    newword = words[i]
    if not check(prevword,newword):
      print(prevword, newword)
      return False
    else:
      prevword = words[i]
  return True
​
def check(prev, new):
  if abs(len(new)-len(prev)) >= 2:
    return False
  elif len(new) != len(prev):
    if len(new) < len(prev):
      if prev.startswith(new) or prev.endswith(new):
        return True
      else:
        diff=0
        for i in range(len(new)):
          if new[i] != prev[i]:
            diff = i
            break
        if prev.startswith(new[:diff]) and prev.endswith(new[diff:]):
          return True
        else:
          return False
    if len(new) > len(prev):
      if new.startswith(prev) or new.endswith(prev):
        return True
      else:
        diff=0
        for i in range(len(prev)):
          if new[i] != prev[i]:
            diff = i
            break
        if new.startswith(prev[:diff]) and new.endswith(prev[diff:]):
          return True
        else:
          return False
  elif len(new) == len(prev):
    diff = 0
    for i in range(len(new)):
      if new[i] != prev[i]:
        diff+=1
    return diff==1

