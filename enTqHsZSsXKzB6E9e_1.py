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

def list_to_string(l):
  return ''.join(str(i) for i in l)

