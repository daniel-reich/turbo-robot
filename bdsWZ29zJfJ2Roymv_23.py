"""


Write a function that swaps the first **pair** (1st and 2nd characters) with
the second **pair** (3rd and 4th characters) for every quadruplet substring.

### Examples

    swap_two("ABCDEFGH") ➞ "CDABGHEF"
    
    swap_two("AABBCCDDEEFF") ➞ "BBAADDCCFFEE"
    
    swap_two("munchkins") ➞ "ncmuinhks"
    
    swap_two("FFGGHHI") ➞ "GGFFHHI"

### Notes

Keep **leftover strings** in the same order.

"""

def swap_two(x):
  bal = ''
  rem = len(x) % 4
  if rem:
    bal = x[-rem:]
    x = x[:-rem]
  fin = []
  for a,b in zip(range(0,len(x),4), range(2,len(x),4)):
    fin.append(x[b:b+2])
    fin.append(x[a:a+2])
  finword = ''.join(fin)+bal
  return finword

