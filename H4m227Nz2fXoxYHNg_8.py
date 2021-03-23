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
    t_list = []
    o_t = ""
    for i in lst:
        o_t = str(type(i))
        o_t = o_t.strip("<class ").strip(">").strip("''")
        t_list.append(o_t)
    return t_list

