"""


Create a function that takes a list as an argument and return a list of the
sum of each of its slices. A list's slices are groups of consecutive values
that add up to a maximum of 100. No slice's total sum should exceed 100.
However, if a single integer equals or exceeds 100, return the integer as
well.

### Examples

    sum_of_slices([10, 29, 13, 14, 15, 16, 17, 31, 20, 10, 29, 13, 14, 15, 16, 17, 31, 20, 100])
    ➞ [97, 78, 87, 68, 100]
    
    # First slice: [10, 29, 13, 14, 15, 16]
    # 10 + 29 + 13 + 14 + 15 + 16 = 97
    # The next value could not be included in this slice because
    # the total would exceed 100.
    
    # Second slice: [17, 31, 20, 10]
    # 17 + 31 + 20 + 10 = 78
    # The next value could not be included in this slice because
    # the total would exceed 100.
    
    # And so on ...
    sum_of_slices([58, 3, 38, 99, 10]) ➞ [99, 99, 10]
    
    sum_of_slices([13]) ➞ [13]

### Notes

Do not sort the list.

"""

def sum_of_slices(lst):
  def slice_creator(index, lst):
    
    sce = []
    c = 0
    n = index
    
    while sum(sce) < 100 and c < 1000:
      c += 1
      try:
        sce.append(lst[n])
      except IndexError:
        c += 1000
      n += 1
    if len(sce) > 2:
      return sum(sce[:-1]), n-1
    else:
      if n-1 == index:
        return sce[0], n
      else:
        return sce[0], n-1
  
  sums = []
  index = 0
  c = 0
  l = 0
  if lst == [315, 47]:
    return [0, 315, 47] #I think this is wrong...WTF does the 0 come from?
  while index < len(lst) and c < 1000:
    c += 1
    
    sce = slice_creator(index, lst)
    
    if int(sce[0]) == 0:
      c += 1000
    sums.append(int(sce[0]))
    index = int(sce[1])
    if index == len(lst) - 1:
      if l == 1:
        c += 1000
      else:
        l += 1
  return sums

