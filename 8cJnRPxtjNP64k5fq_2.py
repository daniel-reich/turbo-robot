"""


You will be given a list of dancing couples, with the woman first and man
second, as well as a parameter `"men"` or `"women"`.

  * If the parameter is `"men"`, the men reverse their positions (first moves to last, last moves to first, etc), while women keep their positions.
  * If the parameter is `"women"`, the women reverse their positions, while men keep their positions.

### Examples

    dance([
      [Ana, Bob],
      [Amy, Josh],
      [Lisa, Tim]
    ], men) ➞ [
      [Ana, Tim],
      [Amy, Josh],
      [Lisa, Bob]
    ]
    
    dance([
      [Ana, Bob],
      [Amy, Josh],
      [Lisa, Tim]
    ], women) ➞ [
      [Lisa, Bob],
      [Amy, Josh],
      [Ana, Tim]
    ]

### Notes

Input lists will always be the same length.

"""

def dance(lst, parameter):
  w_po, m_po = [], []
  for i in range(len(lst)):
    w_po.append(lst[i][0])
    m_po.append(lst[i][1])
  if parameter == 'men':
    m_po.reverse()
  else:
    w_po.reverse()
  return [[i, j] for i,j in zip(w_po, m_po)]
