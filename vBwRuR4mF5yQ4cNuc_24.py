"""


Create a function that takes a list of "mostly" numbers, counts the amount of
missing numbers and returns their sum. Watch out for strings!

### Examples

    count_missing_nums(["1", "3", "5", "7", "9"]) ➞ 4
    # 1+1+1+1
    
    count_missing_nums(["7", "3", "1", "9", "5"]) ➞ 4
    
    count_missing_nums(["1", "5", "B", "9", "z"]) ➞ 6

### Notes

The data might be dirty! Clean out any filthy strings.

"""

def count_missing_nums(lst):
  newlst = []
  for i in lst:
    try:
      newlst.append(int(i))
    except ValueError:
      continue
  finallst = []
  for i in range(min(newlst), max(newlst) + 1):
    finallst.append(i)
  return len(finallst) - len(newlst)

