"""


Burrows-Wheeler transform (BWT) is an algorithm which is used in data
compression. Given a string `text`, BWT of `text` is a modified version of the
string with same length as `text`. It can then be used to efficiently find
substrings of `text` (which won't be covered here). We will just find the BWT
of `text`.

  1. Build Burrows-Wheeler-Matrix (BWM) containing all rotations of `text`.
  2. Sort BWM lexicographically ($ < a < b < ... < z).
  3. BWT is the last coloumn of BWM and gets returned.

    # Example with text = "banana$"
    
    # BWM (all rotations of text):
    banana$
    anana$b
    nana$ba
    ana$ban
    na$bana
    a$banan
    $banana
    
    # BWM sorted lexicographically:
    $banana
    a$banan
    ana$ban
    anana$b
    banana$
    na$bana
    nana$ba
    
    # BWT (last coloumn of BWM):
    annb$aa

### Examples

    bw_transform("banana$") ➞ "annb$aa"
    
    bw_transform("mississippi$") ➞ "ipssm$pissii"
    
    bw_transform("acccgtttgtttcaatagatccatcaa$") ➞ "aacc$tacgttctaccatcaatatttgg"

### Notes

Consider `$` as the terminator character at the end of every input `text`.

"""

import pandas as pd
def bw_transform(text):
  l_w=[l for l in text.strip() ]
  y=l_w.copy()
  con=[y]
  for i in range(len(text)-1):
    l_w.insert(len(l_w),l_w[0])
    l_w=l_w[1:]
    v=l_w.copy()
    con.append(v)
  sort=sorted([''.join( l for l in lst )for lst in con ])
  complete=[[l for l in i] for i in sort]
  df=pd.DataFrame(complete).sum()
  return df.iloc[len(text)-1]

