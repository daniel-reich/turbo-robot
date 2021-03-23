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
  def gender_seperator(lst):
    men = []
    women = []
    
    for item in lst:
      women.append(item[0])
      men.append(item[1])
    
    return [women, men]
  def position_reverser(lst):
    return list(reversed(lst))
  
  dancers_by_gender = gender_seperator(lst)
  
  women = dancers_by_gender[0]
  men = dancers_by_gender[1]
  
  if parameter == 'women':
    women = position_reverser(women)
  elif parameter == 'men':
    men = position_reverser(men)
  
  return [list(i) for i in zip(women, men)]

