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

def dance(lst,parameter):
  if parameter == 'men':
    length = len(lst)
    if length%2 == 0:
      for i in range(0,length//2):
        lst[i][1],lst[-(i+1)][1] = lst[-(i+1)][1],lst[i][1]
      return lst
    else:
      for i in range(0,length//2):
        lst[i][1],lst[-(i+1)][1] = lst[-(i+1)][1],lst[i][1]
      return lst
  elif parameter == 'women':
    length = len(lst)
    if length%2 == 0:
      for i in range(0,length//2):
        lst[i][0],lst[-(i+1)][0] = lst[-(i+1)][0],lst[i][0]
      return lst
    else:
      for i in range(0,length//2):
        lst[i][0],lst[-(i+1)][0] = lst[-(i+1)][0],lst[i][0]
      return lst

