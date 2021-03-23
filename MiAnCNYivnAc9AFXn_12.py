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

def changeTypes(lst):
  for i, item in enumerate(lst):
    if type(lst[i]) == str:
      lst[i] = lst[i].capitalize() + '!'
    elif type(lst[i]) == int:
      if lst[i]%2 == 0:
        lst[i] += 1
    else:
      lst[i] = not (lst[i] or False)
  return lst

