"""


Write a function that returns `True` if you can use the letters of the first
string to create the second string. Letters are **case sensitive**.

### Examples

    can_build("aPPleAL", "PAL") ➞ True
    
    can_build("aPPleAL", "apple") ➞ False
    
    can_build("a", "") ➞ True
    
    can_build("aa", "aaa") ➞ False

### Notes

Letters in the first string can be used only once.

"""

def can_build(s1, s2):
    list1, list2 = [letter for letter in s1], [letter for letter in s2]
    for letter in list2:
        if letter in list1:
            list1.remove(letter)
        else:
            return False
    return True

