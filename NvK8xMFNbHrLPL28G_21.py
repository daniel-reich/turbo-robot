"""


Create a function that takes a number as an argument and returns the highest
digit in that number.

### Examples

    highest_digit(379) ➞ 9
    
    highest_digit(2) ➞ 2
    
    highest_digit(377401) ➞ 7

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're really stuck, unlock solutions in the **Solutions** tab.

"""

def highest_digit(num):
  num_list = list(str(num))
  max = 0
  for n in num_list:
    if int(n) > max:
      max = int(n)
  return max

