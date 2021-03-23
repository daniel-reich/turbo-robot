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
  X_ancestors = [X]
  Y_ancestors = [Y]
  not_top_level = []
  for lst in folders.values():
    for folder in lst:
      not_top_level.append(folder)
  for f in folders:
    if X in folders[f]:
      X_ancestors.append(f)    # closest ancestor of X
    if Y in folders[f]:
      Y_ancestors.append(f)    # closest ancestor of Y
  
  while X_ancestors[-1] in not_top_level:    # find all higher level ancestors of X
    for f in folders:
      if X_ancestors[-1] in folders[f]:
        X_ancestors.append(f)
  while Y_ancestors[-1] in not_top_level:    # find all higher level ancestors of Y
    for f in folders:
      if Y_ancestors[-1] in folders[f]:
        Y_ancestors.append(f)
  
  for folder in X_ancestors:
    if folder in Y_ancestors:
      return folder

