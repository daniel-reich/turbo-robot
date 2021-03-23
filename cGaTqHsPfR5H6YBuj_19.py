"""


Given a list of ingredients `i` and a flavour `f` as input, create a function
that returns the list, but with the elements `bread` around the selected
ingredient.

### Examples

    make_sandwich(["tuna", "ham", "tomato"], "ham") ➞ ["tuna", "bread", "ham", "bread", "tomato"]
    
    make_sandwich(["cheese", "lettuce"], "cheese") ➞ ["bread", "cheese", "bread", "lettuce"]
    
    make_sandwich(["ham", "ham"], "ham") ➞ ["bread", "ham", "bread", "bread", "ham", "bread"]

### Notes

  * You will always get valid inputs.
  * Make two separate sandwiches if two of the same elements are next to each other (see example #3).

"""

def makeSandwich(i,f):
  a=len(i)
  newLst=[]
  for j in range(0,a):
    if(i[j]==f):
      newLst.append("bread")
      newLst.append(i[j])
      newLst.append("bread")
    else:
      newLst.append(i[j])
  return newLst

