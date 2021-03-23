"""


Write a function that splits a string into substrings of size n, adding a
specified delimiter between each of the pieces.

### Examples

    split_and_delimit("bellow", 2, "&") ➞ "be&ll&ow"
    
    split_and_delimit("magnify", 3, ":") ➞ "mag:nif:y"
    
    split_and_delimit("poisonous", 2, "~") ➞ "po~is~on~ou~s"

### Notes

N/A

"""

import re
def split_and_delimit(txt, num, delimiter):
    return_value = '{}'.format(delimiter).join(i for i in re.findall('.'*num,txt))
    value = len(txt) % num
    if value != 0:
        return_value += delimiter + txt[len(txt) - value:]
    return return_value

