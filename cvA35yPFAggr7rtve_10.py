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
  key_list   = [ ]
  un_sorted_value_list = [ ]
  path_to_x  = [ ]
  path_to_y  = [ ]
  for k in folders.keys():
    for i in folders[k]:
      un_sorted_value_list.append (i)
​
​
  for k in folders.keys():
    if k not in un_sorted_value_list:
      top_folder = k 
      break
  sorted_value_list = []
  found_a_sub_set  = True 
  elm              = folders[top_folder]
  while found_a_sub_set:
    sorted_value_list.append (elm)
    elm = []
    for i in sorted_value_list[-1]:
      if i in folders.keys():
        for b in folders[i]:
          elm.append (b)
    if len (elm) == 0 :
      found_a_sub_set = False
  print (sorted_value_list) 
  jump1 = X 
  jump2 = Y
  path_to_x.append (jump1)
  path_to_y.append (jump2)
  while jump1 != top_folder or jump2 !=  top_folder:
    print (jump1,jump2)
    for i in range (len (sorted_value_list)):
      for b in sorted_value_list[i]:
        if b == jump1:
         
          for (k,v) in folders.items():
            if b in v:
              jump1 = k
          path_to_x.append (jump1)
        if b == jump2:  
          
          for (k,v) in folders.items():
            if b in v:
              jump2 = k
          path_to_y.append(jump2)
​
  print (path_to_x)
  print (path_to_y)
  check_ind = abs(len (path_to_x)-len(path_to_y))
​
​
  lenx= len (path_to_x)
  leny = len (path_to_y)
  found = False
  
  if lenx > leny:
    for i in range (lenx-leny,lenx):
        for b in path_to_y:
          if path_to_x[i] == b:
            found = True
            c     = b
            break
        if found:
          break
  elif lenx < leny:
    for i in range (leny-lenx,leny):
      for b in path_to_x:
        if path_to_y [i] == b:
          found = True
          c     = b
          break
      if found:
        break
  else:
    for i in range ( lenx):
      if path_to_x[i] == path_to_y[i]:
        c = path_to_y[i]
        break          
  return c

