"""


Create a function that returns the amount of duplicate characters in a string.
It will be case sensitive and spaces are included. If there are no duplicates,
return `0`.

### Examples

    duplicates("Hello World!") ➞ 3
    # "o" = 2, "l" = 3.
    # "o" is duplicated 1 extra time and "l" is duplicated 2 extra times.
    # Hence 1 + 2 = 3
    
    duplicates("foobar") ➞ 1
    
    duplicates("helicopter") ➞ 1
    
    duplicates("birthday") ➞ 0
    # If there are no duplicates, return 0

### Notes

Make sure to only start counting the second time a character appears.

"""

def duplicates(str1) : 
    l = len(str1)
    x1 = 0 
    l1 = []
    for i in range(l) : 
        x = str1.count(str1[i])
        if (x > 1) and ( str1[i] not in l1) :
            x1 += x-1
            l1.append(str1[i]) 
    return x1

