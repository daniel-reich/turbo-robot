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
    result = True
    for i in s2:
        if i not in s2:
            result = False
        if s1.count(i) < s2.count(i):
            result = False
    if result is False:
        return False
    else:
        return True

