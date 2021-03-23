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
  a=""
  for i in lst:
    if type(i)==str:
      a+=i
    elif type(i)!=str:
      i=str(i)
      a+=i
  return a

