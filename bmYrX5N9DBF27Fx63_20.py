"""


The factors said to have the greatest impact on someone's mood are: weather,
meals, and sleep. Your task is, given a list of sublists of different values
for: Mood, Weather, Meals, and Sleep, determine which other variable has had
the greatest impact on the mood.

### Examples

    greatest_impact([
      [1, 1, 3, 10],
      [1, 1, 3, 10],
      [1, 1, 3, 10]
    ]) ➞ "Weather"
    
    # As it was always low but all others were high.
    
    greatest_impact([
      [10, 10, 3, 10],
      [10, 10, 3, 10],
      [10, 10, 3, 10]
    ]) ➞ "Nothing"
    
    # As all were always high.

### Notes

The mood will always go from 1 to 10, the weather will always go from 1 to 10,
the meals will always go from 1 to 3, and the sleep will always go from 1 to
10. In cases of mood and weather, 1 is negative and 10 is positive. All
sublists values will be in the order `[Mood, Weather, Meals, Sleep]`.

"""

def greatest_impact(lst):
  # lst in format: [Mood, Weather, Meals, Sleep]
  factor_list = []
  elm         = 0 
  for x in range (4):
    for y in range (len (lst)):
      elm += int (lst[y][x])
    if x == 2:
      elm*= 10/3
    factor_list.append (elm)
    elm = 0 
  factor_list = factor_list[1:]
  avg = sum (factor_list)//3
  print ('A',avg)
  highest_diff = abs (factor_list[0] - avg)
​
  same_num = 0 
  for i in factor_list:
    print ('highest_diff:',highest_diff)
    if highest_diff == abs(i-avg):
      print ('Abs',abs (i-avg))
      same_num += 1
    if abs (i - avg) > highest_diff:
      highest_diff = abs (i-avg)
  
  print(factor_list)  
  print ( highest_diff)
  print (same_num)
  
  try:
    index = factor_list.index(highest_diff+avg)
    
  except:
    index = factor_list.index(abs(highest_diff-avg))
  print (index)
  if same_num != 3: 
    if index == 0:
      return 'Weather'
    elif index == 1:
      return 'Meals'
    elif index == 2:
      return 'Sleep'
  else:
    return 'Nothing'

