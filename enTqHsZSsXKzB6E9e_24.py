"""


Create a function that takes a list of numbers or letters and returns a
string.

### Examples

    list_to_string([1, 2, 3, 4, 5, 6]) ➞ "123456"
    
    list_to_string(["a", "b", "c", "d", "e", "f"]) ➞ "abcdef"
    
    list_to_string([1, 2, 3, "a", "s", "dAAAA"]) ➞ "123asdAAAA"

### Notes

N/A

"""

def list_to_string(lst):
  lst2 = []
  for n in lst:
    lst2.append(str(n))
  tpl = tuple(lst2)
  x = ''.join(tpl)
  return x

