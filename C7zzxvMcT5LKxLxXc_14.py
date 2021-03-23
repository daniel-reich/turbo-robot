"""


This is a reverse-coding challenge. Create a function that outputs the correct
list from the input. Use the following examples to crack the code.

### Examples

    decode("hello") ➞ [5, 2, 9, 9, 3]
    
    decode("wonderful") ➞ [11, 3, 2, 1, 2, 6, 3, 9, 9]
    
    decode("something challenging") ➞ [7, 3, 10, 2, 8, 5, 6, 2, 4, 5, 18, 5, 16, 9, 9, 2, 2, 4, 6, 2, 4]

### Notes

N/A

"""

from string import ascii_lowercase as a
​
def decode(txt):
    abc = a[13:-3]+a[-3:-1]+' '+a[-1]+a[:3]+a[3:13]
    x = [x for x in range(19)]
    nums = x[2:12]+x[3:6]+x[15:]+x[1:11]
    encrypt = dict(zip(abc, nums))
    res = [encrypt[x.lower()]+4 if x.isupper() else encrypt[x] for x in txt]
    return res

