"""


 _What do the numbers 4, 6, 8, 9 and 0 have in common? They all have holes in
them! Notice how the number 8 contains not one, but two holes._

Given a list of numbers, sort the list in accordance to how many holes occur
in the number. It should be sorted in **ascending order**.

### Examples

    holey_sort([44, 4, 444, 4444]) ➞ [4, 44, 444, 4444]
    
    holey_sort([100, 888, 1660, 11]) ➞ [11, 100, 1660, 888]
    
    holey_sort([8, 121, 41, 66]) ➞ [121, 41, 8, 66]

### Notes

  * If two numbers have the same number of holes in them, sort them by the order they first appeared in.
  * Despite the number 0 appearing to have _two holes_ in certain fonts, it will only have **one hole** for the purposes of this challenge.

"""

def holey_sort(lst):
  def holes(num):
    dig_holes = {4: 1, 6: 1, 8: 2, 9: 1, 0: 1}
    digits = [int(i) for i in str(num)]
​
    holes = 0
​
    for digit in digits:
      if digit in dig_holes.keys():
        holes += dig_holes[digit]
    
    return holes
  def sorrt(key, holes):
​
    hole_amounts = sorted(list(holes.keys()))
    srrted = []
    
    for amount in hole_amounts:
      to_add = holes[amount]
      for item in lst:
        if item in to_add:
          srrted.append(item)
    
    return srrted
​
  num_of_holes = {}
​
  for num in lst:
    hole_amount = holes(num)
    if hole_amount not in num_of_holes.keys():
      num_of_holes[hole_amount] = [num]
    else:
      num_of_holes[hole_amount].append(num)
  
  return sorrt(lst, num_of_holes)

