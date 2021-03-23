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
  result = [s[i-1:i] * i for i in range(1,len(s) +1)]
  return "-".join([i.title() for i in result])

