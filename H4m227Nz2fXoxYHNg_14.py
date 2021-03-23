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
  n = []
  for i in lst:
    if type(i) == int:
      n.append('int')
    elif type(i) == str:
      n.append('str')
    elif type(i) == list:
      n.append('list')
    elif type(i) == bool:
      n.append('bool')
    elif type(i) == []:
      print(type(i))
      n.append('NoneType')
    elif type(i) == float:
      n.append('float')
    elif type(i) == dict:
      n.append('dict')
    else:
      print(type(i))
      n.append('NoneType')
  return n

