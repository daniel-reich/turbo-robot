"""


Create a function that returns `True` if each pair of adjacent numbers in a
list shares **at least one digit** and `False` otherwise.

### Examples

    shared_digits([33, 53, 6351, 12, 2242, 44]) ➞ True
    # 33 and 53 share 3, 53 and 6351 share 3 and 5, etc.
    
    shared_digits([1, 11, 12, 13, 14, 15, 16]) ➞ True
    
    shared_digits([33, 44, 55, 66, 77]) ➞ False
    
    shared_digits([1, 12, 123, 1234, 1235, 6789]) ➞ False

### Notes

N/A

"""

def shared_digits(lst):
    for i in range(1, len(lst)):
        if len(set(str(lst[i-1])) & set(str(lst[i]))) == 0:
            return False
    return True

