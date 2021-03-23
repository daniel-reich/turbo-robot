"""


Create a function that takes date in the format **yyyy/mm/dd** as an input and
returns `"Bonfire toffee"` if the date is October 31, else return `"toffee"`.

### Examples

    halloween("2013/10/31") ➞ "Bonfire toffee"
    
    halloween("2012/07/31") ➞ "toffee"
    
    halloween("2011/10/12") ➞ "toffee"

### Notes

N/A

"""

import re
​
def halloween(dt):
    return "Bonfire toffee" if re.search('10/31', dt) else "toffee"

