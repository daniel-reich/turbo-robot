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
    d = {type(True):'bool',
         type(22):'int',
         type(2.1):'float',
         type('abc'):'str',
         type([1]):'list',
         type({}): 'dict',
         type(None):'NoneType'}
    return [(d[type(x)]) for x in lst]

