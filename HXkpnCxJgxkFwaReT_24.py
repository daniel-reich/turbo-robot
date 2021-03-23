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
    final_list = []
    final = []
    my_list = [int, str, bool, list, tuple, dict]
    for i in range (0,len(args)):
        final_list.append(type(args[i]))
    #print(final_list)
    int_count = final_list.count(int)
    final.append(int_count)
    str_count = final_list.count(str)
    final.append(str_count)
    bool_count = final_list.count(bool)
    final.append(bool_count)
    list_count = final_list.count(list)
    final.append(list_count)
    tuple_count = final_list.count(tuple)
    final.append(tuple_count)
    dict_count = final_list.count(dict)
    final.append(dict_count)
    
    return final
    
    
​
print(count_datatypes(1, 45, "Hi", False))

