"""


Create a function that takes a string `s` and modifies the given string as per
the below examples:

### Examples

    mumbling("MubAshIr") ➞ "M-Uu-Bbb-Aaaa-Sssss-Hhhhhh-Iiiiiii-Rrrrrrrr"
    
    mumbling("maTT") ➞ "M-Aa-Ttt-Tttt"
    
    mumbling("EdaBit") ➞ "E-Dd-Aaa-Bbbb-Iiiii-Tttttt"

### Notes

N/A

"""

def mumbling(s):
  return '-'.join((i*idx).title() for idx, i in enumerate(s, 1))

