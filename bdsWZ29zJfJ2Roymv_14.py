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

def swap_two(txt):
  txt = list(txt)
  try:
    for i in range(0,len(txt),+4):
      txt[i+2],txt[i+3],txt[i],txt[i+1] = txt[i:i+4]
  except ValueError:
    return "".join(txt)
  return "".join(txt)

