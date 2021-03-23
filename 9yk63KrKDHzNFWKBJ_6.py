"""


A folder system on a computer might look something like the picture below.

![](https://edabit-challenges.s3.amazonaws.com/folders_smaller.png)

In this challenge, folder systems will be represented by dictionaries where
the keys are folders X and the value at X is the list of subfolders of X. For
example, the picture above becomes the dictionary.

    {
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }

The inputs for this challenge will be:

  * A dictionary representing a folder system.
  * Two folders, X and Y.

 **Write a function that decides whether "X is inside Y"** (in the
illustration, this means that you can travel down from Y to X).

### Examples

    is_it_inside({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "B",  "A") ➞ True
    
    is_it_inside({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "B",  "D") ➞ False
    
    is_it_inside({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "I",  "D") ➞ True
    
    is_it_inside({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "A", "K") ➞ False
    
    is_it_inside({
      "A": ["B", "C", "D"],
      "B": ["E", "F"],
      "D": ["G", "H"],
      "G": ["I", "J"],
      "H": ["K"]
    }, "D", "D") ➞ True

### Notes

  * All the examples above use the folder system in the illustration, but the tests will use other folder systems as well.
  * For the purposes of this challenge, any folder is inside itself, as in the last example.
  * This challenge has a [part 2](https://edabit.com/challenge/cvA35yPFAggr7rtve).

"""

def is_it_inside(f,x,y):
    if x==y:return True
    l = f.get(y)
    try:
     if x in l:return True
    except:
        return False
    for i in l:
        if i in f.keys():
            l2=[j for j in f.get(i)]
            if x in l2:return True
            for k in l2:
              if k in f.keys():
                 if x in f.get(k):return True
    return False

