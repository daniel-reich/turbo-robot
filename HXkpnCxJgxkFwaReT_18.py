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
    l = []
    int_count = 0
    str_count = 0
    bool_count = 0
    list_count = 0
    tuple_count = 0
    dictionary_count = 0
    for a in args:
        if type(a) is dict:
            dictionary_count += 1
        if type(a) is int:
            int_count += 1
        if type(a) is str:
            str_count += 1
        if type(a) is bool:
            bool_count += 1
        if type(a) is list:
            list_count += 1
        if type(a) is tuple:
            tuple_count += 1
    return [int_count, str_count, bool_count, list_count, tuple_count, dictionary_count]

