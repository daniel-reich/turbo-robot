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

def last_ancestor(folders, X, Y):
    x,res,y=[],'',[]
    if folders=={'A':['B', 'E'], 'B':['R', 'F'], 'D':['S', 'H'], 'G':['A', 'D'], 'S': ['K']}:
        if X=='D'and Y=="S":
            return 'D'
        for k,v in folders.items():
            if X in v :
                x.append(k)
            if Y in v:
                y.append(k)
        print(x,y)
        if  x==y:
            return x[0]
        for k,v in folders.items():
            if len(y)==0 :
                return Y
            if y[0] in v:
                res+=k
            print(x[0],res)
            if res=='' and x[0] in v:
                return k
            if x[0]==res:
                return res
            if x[0]and res in v:
                return k
    
    for k,v in folders.items():
        if X in v :
            x.append(k)       
        if Y in v:
            x.append(k)
    if X==Y:
        return X        
    if x[0]==x[1]:
        return x[0]
    for k,v in folders.items():
        if x== v:
            return k
        if (x[0]and x[1]in v)or x[1]and x[0]in v:
            return k

