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

list_values_types = lambda lst: [type(i).__name__ for i in lst]
