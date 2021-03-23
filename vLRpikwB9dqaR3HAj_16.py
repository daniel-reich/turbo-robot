"""


Given two lists `smlst` and `biglst`, we say smlst is an _ordered sublist_ of
`biglst` if all the elements of `smlst` can be found in `biglst`, and _in the
same order_.

Examples:

  * `[4, 3, 2]` is an ordered sublist of `[5, 4, 3, 2, 1]`.
  * `[5, 3, 1]` is an ordered sublist of `[5, 4, 3, 2, 1]`.
  * `[5, 3, 1]` is **not** and ordered sublist of `[1, 2, 3, 4, 5]` since elements are not in the same - `[1, 2, 3]` is an ordered sublist of `[3, 2, 1, 2, 3]`.

Write a function that, given lists `smlst` and `biglst`, decides if `smlst` is
an ordered sublist of `biglst`.

### Examples

    is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]) ➞ True
    
    is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]) ➞ True
    
    is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]) ➞ False
    
    is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]) ➞ True

### Notes

Be careful of examples like the fourth example, where the elements of `smlst`
appear multiple times in `biglst`.

"""

def is_ord_sub(smlst, biglst):
  
  Sublist = []
  
  BC = 0
  BL = len(biglst)
  
  SC = 0
  SL = len(smlst)
  
  while (SC < SL) and (BC < BL):
    
    Wanted = smlst[SC]
    Checking = biglst[BC]
    
    if (Wanted == Checking):
      Sublist.append(Wanted)
      SC += 1
      BC += 1
    else:
      BC += 1
  
  Test_1A = len(smlst)
  Test_1B = len(Sublist)
  
  if (Test_1A == Test_1B):
    return True
  else:
    return False

