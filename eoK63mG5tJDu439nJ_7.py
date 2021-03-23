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

def get_prefix_length(long, short):
  prefix = 0
  while prefix < len(short) and long[prefix] == short[prefix]:
    prefix += 1
  return prefix
    
def linkable(s1, s2):
  if len(s2) > len(s1):
    s1, s2 = s2, s1
  prefix_len  = get_prefix_length(s1, s2)
  suffix_len  = get_prefix_length(s1[::-1], s2[::-1])
  return len(s1) - (suffix_len + prefix_len) <= 1 
  
​
def isWordChain(words):
  return all(linkable(w1, w2) for w1, w2 in zip(words, words[1:]))

