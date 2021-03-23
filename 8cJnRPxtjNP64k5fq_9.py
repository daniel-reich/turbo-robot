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
  women = []
  men = []
  final_list =[]
  for i in range(len(lst)):
    women.append(lst[i][0])
    men.append(lst[i][1])
  
  if parameter == 'men':
    for i, j in zip(men[::-1],women):
      final_list.append([j,i])
​
  if parameter == 'women':
    for i, j in zip(men,women[::-1]):
      final_list.append([j,i])
  
  return final_list

