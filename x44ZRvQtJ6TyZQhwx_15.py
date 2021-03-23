"""


A **pandigital** number contains all digits (0-9) at least once. Write a
function that takes an integer, returning `True` if the integer is pandigital,
and `False` otherwise.

### Examples

    is_pandigital(98140723568910) ➞ True
    
    is_pandigital(90864523148909) ➞ False
    # 7 is missing.
    
    is_pandigital(112233445566778899) ➞ False

### Notes

Think about the properties of a pandigital number when all duplicates are
removed.

"""

def is_pandigital(n : int) -> bool:
    bool0, bool1, bool2, bool3, bool4, bool5, bool6, bool7, bool8, bool9 = \
    False, False, False, False, False, False, False, False, False, False
    for i in str(n):
        if i == "0":
            bool0 = True
        if i == "1":
            bool1 = True
        if i == "2":
            bool2 = True
        if i == "3":
            bool3 = True
        if i == "4":
            bool4 = True
        if i == "5":
            bool5 = True
        if i == "6":
            bool6 = True
        if i == "7":
            bool7 = True
        if i == "8":
            bool8 = True
        if i == "9":
            bool9 = True
    return (bool0 and bool1 and bool2 and bool3 and bool4 and bool5 and bool6 and bool7 and bool8 and bool9) == True

