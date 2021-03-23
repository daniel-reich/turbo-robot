"""


In the **Code** tab is a function which is meant to return how many
_uppercase_ letters there are in a list of various words. Fix the list
comprehension so that the code functions normally!

### Examples

    count_uppercase(["SOLO", "hello", "Tea", "wHat"]) ➞ 6
    
    count_uppercase(["little", "lower", "down"]) ➞ 0
    
    count_uppercase(["EDAbit", "Educate", "Coding"]) ➞ 5

### Notes

Check the **Resources** for some helpful tutorials on list comprehensions.

"""

def count_uppercase(lst):
  return sum(letter.isupper() for word in lst for letter in word )

