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
  lst = []
  for i in range(0, len(txt), 2):
    lst.append(txt[i:i+2])
  for i in range(1, len(lst), 2):
    if len(lst[i]) > 1:
      x = lst[i]
      y = lst[i-1]
      lst[i] = y
      lst[i-1] = x
  return "".join(lst)

