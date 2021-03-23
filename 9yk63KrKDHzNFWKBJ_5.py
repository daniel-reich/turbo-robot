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

def is_it_inside(folders,X,Y):
  step = X
  print(X)
  print(Y)
  print(folders)
  for i in range(len(folders)):
    if step == Y:
      result= True
      break
    else:
      result = False  
    for keys in folders:
      if step in folders[keys]:
        step = keys
        break
        print(step)
  print(result) 
  return result

