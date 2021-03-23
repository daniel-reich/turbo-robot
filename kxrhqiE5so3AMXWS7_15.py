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

def get_number_of_apples(n, p):
  apples = int(n-n*int(p.strip('%'))*0.01)
  return apples if n and apples else "The children didn't get any apples"

