"""


Given two strings, `first_name` and `last_name`, return a single string in the
format "last, first".

### Examples

    concat_name("First", "Last") ➞ "Last, First"
    
    concat_name("John", "Doe") ➞ "Doe, John"
    
    concat_name("Mary", "Jane") ➞ "Jane, Mary"

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def concat_name(first_name, last_name):
  return "{}, {}".format(last_name,first_name)

