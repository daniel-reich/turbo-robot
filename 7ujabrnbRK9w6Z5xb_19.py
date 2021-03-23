"""


Create a function that takes a list of integers and strings. Convert integers
to strings and return the new list.

### Examples

    parse_list([1, 2, "a", "b"]) ➞ ["1", "2", "a", "b"]
    
    parse_list(["abc", 123, "def", 456]) ➞ ["abc", "123", "def", "456"]
    
    parse_list([1, 2, 3, 17, 24, 3, "a", "123b"]) ➞ ["1", "2", "3", "17", "24", "3", "a", "123b"]
    
    parse_list([]) ➞ []

### Notes

N/A

"""

def parse_list(lst):
  list_str = []
  for i in lst:
    i = str(i)
    list_str.append(i)
    
  return list_str

