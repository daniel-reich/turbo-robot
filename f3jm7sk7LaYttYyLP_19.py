"""


Create a function that takes a number (from 1 - 60) and returns a
corresponding `string` of hyphens.

### Examples

    num_to_dashes(1) ➞ "-"
    
    num_to_dashes(5) ➞ "-----"
    
    num_to_dashes(3) ➞ "---"

### Notes

  * You will be provided integers ranging from 1 to 60.
  * Don't forget to return your result as a `string`.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def num_to_dashes(num):
  a = "-"
  while num > 1:
    a = a + "-"
    num -= 1
  return a

