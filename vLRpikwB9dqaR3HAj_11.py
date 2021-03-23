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
  sub_counter = 0
  current_index = 0
  startIndex = 0
  for i in smlst:
    for j in biglst[startIndex:]:
      if i == j:
        startIndex = current_index
        sub_counter += 1
        current_index += 1
        break
​
      current_index += 1
  
  return sub_counter == len(smlst)

