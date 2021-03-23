"""


Write a function that returns `True` if every consecutive sequence of **ones**
is followed by a consecutive sequence of **zeroes** of the same length.

### Examples

    same_length("110011100010") ➞ True
    
    same_length("101010110") ➞ False
    
    same_length("111100001100") ➞ True
    
    same_length("111") ➞ False

### Notes

N/A

"""

import re
def same_length(txt):
    return False if len(re.compile(r"1+").findall(txt)) != len(re.compile(r"0+").findall(txt)) else False not in [len(i[0]) == len(i[1]) for i in zip(re.compile(r"1+").findall(txt), re.compile(r"0+").findall(txt))]

