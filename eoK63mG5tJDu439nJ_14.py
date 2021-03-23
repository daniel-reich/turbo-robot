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
  is_chain = False
  for i in range(len(words)-1):
    s1 = words[i]
    s2 = words[i+1]
    num_hit = num_hits(s1, s2)
    if len(s2) == len(s1) + 1 and num_hit == len(s1):
      is_chain = True
    elif len(s2) == len(s1) - 1 and num_hit == len(s1) - 1:
      is_chain = True
    elif len(s2) == len(s1) and num_hit == len(s1) - 1:
      is_chain = True
    else:
      return False
  return is_chain
​
def num_hits(s1, s2):
    num_hit = 0
    for char in s1:
        if char in s2:
            num_hit += 1
    return num_hit

