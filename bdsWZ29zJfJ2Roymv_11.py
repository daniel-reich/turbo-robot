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
  chars = list(txt)
  new = []
  i = 0
  while i < len(chars)-3:
    new.extend([chars[i+2], chars[i+3]])
    new.extend([chars[i], chars[i+1]])
    i += 4
  tail = len(txt)%4
  if tail > 0:
    chunk = chars[-tail:]
    new.extend(chunk)
  s = ''.join(new)
  return s

