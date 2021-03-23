"""


Write a function that sorts a given list in an aletrnative fashion. The result
should be a list sorted in ascending order (number then letter). Lists will
contain equal amounts of integer numbers and single characters.

### Examples

    alternate_sort(["a", "b", "c", 1, 2, 3]) ➞ [1, "a", 2, "b", 3, "c"]
    
    alternate_sort([-2, "f", "A", 0, 100, "z"]) ➞ [-2, "A", 0, "f", 100, "z"]
    
    alternate_sort(["X", 15, 12, 18, "Y", "Z"]) ➞ [12, "X", 15, "Y", 18, "Z"]

### Notes

N/A

"""

def alternate_sort(lst):
  def sort_nums_l8rs(lst):
    numbers = []
    letters = []
    
    for item in lst:
      try:
        numbers.append(int(item))
      except ValueError:
        letters.append(item)
    
    return [sorted(numbers), sorted(letters)]
  def combine(l1, l2):
    combined = []
    
    if len(l1) > len(l2):
      for n in range(len(l2)):
        combined.append(l1[n])
        combined.append(l2[n])
      for n in range(len(l2), len(l1)):
        combined.append(l1[n])
    elif len(l1) < len(l2):
      for n in range(len(l1)):
        combined.append(l1[n])
        combined.append(l2[n])
      for n in range(len(l1), len(l2)):
        combined.append(l2[n])
    else:
      for n in range(len(l1)):
        combined.append(l1[n])
        combined.append(l2[n])
    
    return combined
  
  nums, l8rs = sort_nums_l8rs(lst)
  
  return combine(nums, l8rs)

