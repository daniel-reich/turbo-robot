"""


Create a function that takes a list `lst` and returns the types of values
(data types) in a new list.

### Examples

    list_values_types([1, 10]) ➞ ["int", "int"])
    
    list_values_types([["hello" , 1] , 10]) ➞ ["list", "int"])
    
    list_values_types(["shashwat", 10, 90]) ➞ ["str", "int", "int"])

### Notes

Check the **Resources** tab for help if needed.

"""

def list_values_types(lst):
  o = []
  for i in lst:
    t = str(type(i))
    lt = t.find("'")
    rt = t.rfind("'")
    o.append(t[lt+1:rt])
  return o

