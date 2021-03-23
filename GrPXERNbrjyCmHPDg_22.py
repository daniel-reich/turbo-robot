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
    newcount = 0
    new = str(txt)
    se = set(new)
    l= []
    for i in se:
        sub = str(i)
        #print(sub)
        count = new.count(sub)
        #print('count',count)
        if count>=2:
            newcount += 1
            #print('newcount',newcount)
            l.append(newcount)
        #print(l)
    return newcount

