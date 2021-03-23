"""


Create a function that takes a string and returns the number of alphanumeric
characters that occur more than once.

### Examples

    duplicate_count("abcde") ➞ 0
    
    duplicate_count("aabbcde") ➞ 2
    
    duplicate_count("Indivisibilities") ➞ 2
    
    duplicate_count("Aa") ➞ 0
    # Case sensitive

### Notes

  * Duplicate characters are case sensitive.
  * The input string will contain only alphanumeric characters.

"""

def duplicate_count(txt):
    lst=[]
    lst2=[]
    for i in range(len(txt)):
        lst.append(txt[i])
        if lst.count(lst[i])>1:
            lst2.append(lst[i])
    return len(set(lst2))

