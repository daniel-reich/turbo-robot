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
def get_number_of_apples(n, p):
    new_p=p.replace('%','')
    new_p=int(new_p)
    apples_eaten=math.ceil((new_p*n)/100)
    if n-apples_eaten>0:
        return n-apples_eaten
    else:
        return 'The children didn\'t get any apples'

