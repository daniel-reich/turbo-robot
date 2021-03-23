"""


Create a function which validates whether a given number exists, and could
represent a real life quantity. Inputs will be given as a string.

### Examples

    valid_str_number("3.2") ➞ True
    
    valid_str_number("324") ➞ True
    
    valid_str_number("54..4") ➞ False
    
    valid_str_number("number") ➞ False

### Notes

Accept numbers such as `.5` and `0003`.

"""

import re
def valid_str_number(s):
    return bool(re.fullmatch('\d*\.?\d*', s))

