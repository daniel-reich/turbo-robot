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

def valid(st1,st2):
  big,small = (st1,st2)  if len(st1) > len(st2)  else  (st2,st1)
  print(big,small)
  s2b_map = [None for i in range(len(big))]
  
  for i,s in enumerate(small):
    for j,b in enumerate(big):
      if j<i:
        continue
      if b == s and s2b_map[j] == None:
        s2b_map[j] = i
        break
​
  print(s2b_map)  
​
  diffs = 0
  last = None
  for m in s2b_map:
    if m == None:
      diffs += 1
    elif last != None and m<last:
        diffs += 1
    last = m
  
​
  print(s2b_map)
  print(diffs)
  return diffs == 1
​
    
def isWordChain(words):
  first = words[0]
  for word in words[1:]:
    if not valid(first,word):
      return False
    first = word
  return True

