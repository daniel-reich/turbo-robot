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
    lst_1 = [0, 0, 0, 0, 0, 0]
​
    for i in args:
        if type(i) == int:
            lst_1[0] += 1
        elif type(i) == str:
            lst_1[1] += 1
        elif type(i) == bool:
            lst_1[2] += 1
        elif type(i) == list:
            lst_1[3] += 1
        elif type(i) == tuple:
            lst_1[4] += 1
        elif type(i) == dict:
            lst_1[5] += 1
        
    return lst_1

