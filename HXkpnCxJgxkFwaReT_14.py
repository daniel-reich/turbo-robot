"""


Given a function that accepts **unlimited** arguments, check and count how
many data types are in those arguments. Finally return the total in a list.

List order is:

    [int, str, bool, list, tuple, dictionary]

### Examples

    count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]
    
    count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]
    
    count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]
    
    count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]

### Notes

If no arguments are given, return `[0, 0, 0, 0, 0, 0]`

"""

def count_datatypes(*args):
​
    type_count = [0, 0, 0, 0, 0, 0]
​
    for arg in args:
        if isinstance(arg, bool):
            type_count[2] = type_count[2] + 1
            continue
        elif isinstance(arg, int):
            type_count[0] = type_count[0] + 1
            continue
        elif isinstance(arg, str):
            type_count[1] = type_count[1] + 1
            continue
        elif isinstance(arg, list):
            type_count[3] = type_count[3] + 1
            continue
        elif isinstance(arg, tuple):
            type_count[4] = type_count[4] + 1
            continue
        elif isinstance(arg, dict):
            type_count[5] = type_count[5] + 1
            continue
​
    return type_count

