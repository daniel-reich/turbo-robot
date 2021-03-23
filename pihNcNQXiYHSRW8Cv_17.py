"""


Create a function that returns a list of strings sorted by length in
**ascending** order.

### Examples

    sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
    
    sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
    
    sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
    
    sort_by_length([]) ➞ []

### Notes

  * Strings will have unique lengths, so don't worry about comparing two strings with identical length.
  * Return an empty array if the input array is empty (see example #4).

"""

def sort_by_length(lst):
  if len(lst) == 0:
    return []
​
  str_list = [lst[0]]
  
  for i in lst[1:]:
    idx = -1
    for j in str_list:
      idx += 1
      if len(i) < len(j):
        str_list.insert(idx,i)
        break
      if len(str_list) == (idx+1):
        str_list.insert(idx+1,i)
        break
  
  return str_list

