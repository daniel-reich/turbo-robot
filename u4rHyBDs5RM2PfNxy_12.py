"""


Create a function that counts the number of blocks of **two or more** adjacent
`1`s in a list.

### Examples

    count_ones([1, 0, 0, 1, 1, 0, 1, 1, 1]) ➞ 2
    # Two instances: [1, 1] (middle) and [1, 1, 1] (end)
    
    count_ones([1, 0, 1, 0, 1, 0, 1, 0]) ➞ 0
    
    count_ones([1, 1, 1, 1, 0, 0, 0, 0]) ➞ 1
    
    count_ones([0, 0, 0]) ➞ 0

### Notes

  * A single 1 by itself (surrounded by a zero on its left and right), does **not** count towards the total (see first example).
  * Each input will contain only zeroes and ones.

"""

def count_ones(lst): #w/o built-in
    def l(it):
        c = 0
        while it:
            c += 1
            it = it[1:]
        return c
    d = {0: "0", 1: "1"}
    st = ""
    for i in lst:
        st += d[i]
    s, tmp = [], ""
    for i in st:
        if i == "0":
            s += [tmp]
            tmp = ""
        else:
            tmp += i
    if tmp:
        s += [tmp]
    count = 0
    for x in s:
        if l(x) > 1:
            count += 1
    return count

