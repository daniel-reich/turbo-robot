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
  def change(sword, eword):
​
    slist = list(sword)
    elist = list(eword)
​
    changed = 0
    
    for n in range(0, len(slist)):
​
      sl8r = slist[n]
      el8r = elist[n]
​
      if sl8r != el8r:
        changed += 1
    
    if changed > 1:
      return False
    elif changed < 1:
      return False
    else:
      return True
  def add_sub(sword, eword):
    
    slist = list(sword)
    elist = list(eword)
​
    slen = len(slist)
    elen = len(elist)
​
    if elen == slen + 1:
      return True
    elif elen == slen - 1:
      p = True
      ns = []
      for l8r in elist:
        
        for n in range(0, len(slist)):
          sl8r = slist[n]
​
          if sl8r == l8r:
            ns.append(n)
        
      sns = sorted(ns)
      stdword = ''
      
      for item in sns:
        l8r = slist[item]
        stdword += l8r
      
      if ns == sns and stdword == eword:
        return True
      else:
        return False
    else:
      return False
​
  possible = True
​
  n = 0
​
  while possible == True:
​
    word1 = words[n]
    try:
      word2 = words[n + 1]
    except IndexError:
      return possible
    
    list1 = list(word1)
    list2 = list(word2)
​
    len1 = len(list1)
    len2 = len(list2)
​
    if len1 == len2:
      possible = change(word1, word2)
    else:
      possible = add_sub(word1, word2)
​
    n += 1
​
  return possible

