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

def value(char):
  if type(char) == str:
    if char.isdigit():
      return "{}!".format(char)
    else:
      return "{}!".format(char.capitalize())
  elif type(char) == int:
    if char % 2 == 0:
      return char + 1
    else:
      return char
  elif char == True:
    return False
  else:
    return True
  
def change_types(lst):
  new_list = [value(char) for char in lst]
  return new_list

