"""


Create a function that returns the original value from a list with too many
sub-lists.

### Examples

    de_nest([[[[[[[[[[[[3]]]]]]]]]]]]) ➞ 3
    
    de_nest([[[[[[[True]]]]]]]) ➞ True
    
    de_nest([[[[[[[[[[[[[[[[["edabit"]]]]]]]]]]]]]]]]]) ➞ "edabit"

### Notes

You only need to retrieve one element.

"""

def de_nest(lst):
  l = lst[0] #Define 'l' so a while loop can be used
  while isinstance(l,list): #repeat until l is not a list
    l = l[0] 
    #This is a neat little trick in recursion, you can keep diving
    #into list by just taking the 0 index of itself!
  return l

