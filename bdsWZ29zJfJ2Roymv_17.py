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
  result, x= "", 0
  while x < len(txt):
    a, b = "", ""
    if x + 4 <= len(txt):
      a += txt[x]
      a += txt[x+1]
      b += txt[x+2]
      b += txt[x+3]
      a, b = b, a
      result += a + b
      x += 4
    else:
      result += txt[x]
      x += 1
  return result

