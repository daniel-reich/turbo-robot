"""
Create a function that changes all the elements in a list as follows:

  * Add 1 to all **even integers** , nothing to odd integers.
  * Concatenates "!" to all **strings** and make the first letter of the word a capital letter.
  * Changes all `boolean` values to its opposite.

### Examples

    change_types(["a", 12, True]) ➞ ["A!", 13, False]
    
    change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]
    
    change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]

### Notes

  * There won't be any float values.
  * You won't get strings with both numbers and letters in them.
  * Although the task may be easy, try keeping your code as clean and as readable as possible!

"""

def change_types(lst):
  res = []
  for i in range(len(lst)):
    elt = lst[i]
    if isinstance(elt,int) and not isinstance(elt,bool):
      if elt%2==0: elt+=1
      res.append(elt)
    elif isinstance(elt,str):
      res.append(elt.capitalize()+"!")
    else:
      res.append(not elt)
  return res

