"""


Write a function that returns `True` if a string consists of **ascending or
ascending AND consecutive** numbers.

### Examples

    ascending("232425") ➞ True
    # Consecutive numbers 23, 24, 25
    
    ascending("2324256") ➞ False
    # No matter how this string is divided, the numbers are not consecutive.
    
    ascending("444445") ➞ True
    # Consecutive numbers 444 and 445.

### Notes

A **number** can consist of any number of digits, so long as the numbers are
adjacent to each other, and the string has at least two of them.

"""

def ascending(txt):
    res =[]
    for i in range(1,len(txt)):
        if len(txt) % i == 0:
            tmp = []
            for j in range(len(txt) // i) :
                tmp.append(int(txt[j*i:(j+1) *i]))
            res.append(tmp)
    for i in res:
        c = True
        for n in range(1, len(i)) :
            if not i[n -1] + 1 == i[n]:
                c = False
        if c:
            return True
    return False

