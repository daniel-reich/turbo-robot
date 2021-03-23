"""


This is a sequel to [part #1](https://edabit.com/challenge/9yk63KrKDHzNFWKBJ),
with the same setup, but a different goal.

A folder system on a computer might look something like the picture below:

![](https://edabit-challenges.s3.amazonaws.com/folders_smaller.png)

In this challenge, folder systems will be represented by dictionaries where
the keys are folders `X` and the value at `X` is the list of subfolders of
`X`.

For example, the picture above becomes the dictionary:

    {
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }

The inputs for this challenge will be:

  * A dictionary representing a folder system.
  * Two folders `X` and `Y`.

Write a function that finds the "smallest" folder containing both `X` and `Y`
(in the illustration, this is the lowest folder for which you can travel down
to both `X` and `Y`; or, if you view the system as a "family tree", this is
the last common ancestor).

### Examples

    last_ancestor({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "B", "C") ➞ "A"
    
    last_ancestor({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "I", "J") ➞ "G"
    
    last_ancestor({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "I", "K") ➞ "D"
    
    last_ancestor({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "D", "I") ➞ "D"
    
    last_ancestor({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "G", "G") ➞ "G"

### Notes

  * All the examples above use the folder system in the illustration, but the tests will use other folder systems as well.
  * For the purposes of this challenge, any folder is inside itself, as in the last two examples.

"""

from itertools import permutations
​
def last_ancestor(folders, X, Y):
​
    keysMaster = list(folders.keys())
    length = len(keysMaster)
    perms = permutations(keysMaster)
    keys = []
    for keys in perms:
        stk = [keys[0]]
        testList = [keys[0]]
        while(len(stk) > 0):
            stkKey = stk.pop()
            keyList = folders.get(stkKey, None)
            for lstKey in keyList:
                testKey = folders.get(lstKey, None)
                if(testKey != None):
                    stk.append(lstKey)
                    testList.append(lstKey)
        if(len(testList) == length):
            break
        
    paths = []
    targets = [X, Y]
    for index in range(len(targets)):
        iters = []
        path = []
        it = iter(keys)
        iters.append(it)
        path.append(keys[0])
        done = False
        while len(iters) > 0:
            it = iters[len(iters) - 1]
            try:
                while True:
                    i = next(it)
                    if(i == targets[index]):
                        if(i not in path):
                            path.append(i)
                        done = True
                        break
                    lst = folders.get(i, None)
                    if(lst != None):
                        it = iter(lst)
                        iters.append(it)
                        if(i not in path):
                            path.append(i)
                        break
            except:
                it = iters.pop()
                path.pop()
            if(done):
                break
        paths.append(path)
        
    res = []
    for node in paths[0]:
        if(node in paths[1]):
           res.append(node)
           
    return res[len(res) - 1]

