"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive ascending** numbers,
otherwise, return `False`.

### Examples

    is_ascending("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_ascending("101112131415") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 10, 11, 12, 13, 14, 15
    
    is_ascending("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_ascending("326325324323") ➞ False
    # Though the numbers (if grouped into 3's) are consecutive but descending.
    
    is_ascending("666667") ➞ True
    # Consecutive numbers: 666 and 667.

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent to each other** , and the string has **at least two** of them.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/Pjffmm9TTr7CxGDRn).

"""

def is_ascending(astring):
    print(astring)
    if astring == '1235':
        print('')
    newlist = []
    for i in range(len(astring)):
        try:
            for j in range(0,len(astring),i):
                newlist.append(astring[j:j+i])
            if is_ascending_list(newlist):
                return True
            newlist = []
        except Exception as e:
            continue
    return False
            
def is_ascending_list(alist):
    for i in range(len(alist)-1):
        if int(alist[i+1]) > int(alist[i]) and int(alist[i+1]) - int(alist[i]) == 1:
            continue
        else:
            return False
    return True

