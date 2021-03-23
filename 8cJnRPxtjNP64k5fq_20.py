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

from operator import itemgetter
def dance(lst, p):
  women = list(map(itemgetter(0),lst))
  men = list(map(itemgetter(1),lst))
  if p == 'men':
    return [[x,y] for x,y in zip(women,men[::-1])]
  else:
    return [[x,y] for x,y in zip(women[::-1],men)]

