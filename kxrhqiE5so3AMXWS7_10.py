"""


A man has `n` number of apples. If he eats a percentage `p` of the apples (if
apples are available), his children will share the remainder of the apples.
Create a function to determine the number of 'whole' apples his children got.
If his children did not get any apples, return `"The children didn't get any
apples"`.

### Examples

    get_number_of_apples(10, "90%") ➞ 1
    
    get_number_of_apples(25, "10%") ➞ 22
    
    get_number_of_apples(0, "10%") ➞ "The children didn't get any apples"

### Notes

`p` will always be given.

"""

import math
​
def get_number_of_apples(n, p):
  
  Number_Text = p.replace("%","")
  Number = int(Number_Text)
  Eaten = round(Number * 0.01, 2)
  Remaining = round(1 - Eaten,2)
  
  Children_Share = math.floor(n * Remaining)
  
  if (Children_Share == 0):
    return "The children didn't get any apples"
  else:
    return Children_Share

