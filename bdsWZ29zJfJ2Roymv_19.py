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
  if len(txt) <= 3:
    return txt
  lst_three = txt[-3:]
  ls = []
  ks = []
  js = []
  zs = []
  bs = []
  asz = []
  st = ''
  for a in txt:
    ls.append(a)
  
  for a in range(0, len(ls),2):
    ks.append(ls[a:a+2])
  
  for a in range(len(ks)):
    if a % 2 != 0:
      js.append(ks[a])
    else:
      zs.append(ks[a])
  for a in js:
    for b in zs:
      if len(a) == len(b):
        z = list(zip(js, zs))
      
  for a in z:
    for b in a:
      asz.append(b)
      
  for a in asz:
    for b in a:
      st += b
  
  first_half = st[:-3]
  end = st[-3]
  ls_two = st[-2:]
  
  if len(txt) % 2 == 0:
    return st
  elif len(txt) % 4 == 1:
    return st + txt[-1]
  else:
    return first_half+ls_two+end

