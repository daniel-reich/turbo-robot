"""


Create a function that takes a list and a string as arguments and return the
index of the string.

### Examples

    find_index(["hi", "edabit", "fgh", "abc"], "fgh") ➞ 2
    
    find_index(["Red", "blue", "Blue", "Green"], "blue") ➞ 1
    
    find_index(["a", "g", "y", "d"], "d") ➞ 3
    
    find_index(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple") ➞ 0

### Notes

  * Don't forget to `return` the result.
  * If you are stuck, find help in the **Resources** tab.
  * The variable for list is `lst`, not `1st`.

"""

def find_index(lst, txt):
    return lst.index(txt)

