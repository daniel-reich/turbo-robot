"""


Create a function which converts an **ordered** number list into a list of
ranges (represented as strings). Note how some lists have some numbers
missing.

### Examples

    numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]
    
    numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]
    
    numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]
    
    numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]

### Notes

  * If there are no numbers consecutive to a number in the list, represent it as only the _string_ version of that number (see example #4).
  * Return an empty list if the given list is empty.

"""

def numbers_to_ranges(lst): #w/o built-in
    d = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}
    if not lst: return []
    y, r = [lst[0]], []
    c = lst[1:]
    while c != []:
        if c[0] - y[-1] == 1:
            y += [c[0]]
            c = c[1:]
        else:
            r += [y]
            y = [c[0]]
            c = c[1:]
    r = r + [y]
    r = [[x[0], x[-1]] for x in r]
    lst = []
    for x in r:
        i = []
        for y in x:
            while y > 0:
                i += [y % 10]
                y //= 10
            lst += [i]
            i = []
    lst = [x[::-1] for x in lst]
    g, new, count = [], [], 0
    for x in lst:
        g += [x]
        count += 1
        if count == 2:
            new += [g]
            count = 0
            g = []
    new = [[[d[z] for z in x] for x in y] for y in new]
    new = [[x[0]] if x[0] == x[-1] else x for x in new]
    s, t, u = "", [], []
    for x in new:
        for y in x:
            for z in y:
                s += z
            t += [s]
            s = ""
        u += [t]
        t = []
    s2, final = "", []
    for x in u:
        for y in x:
            s2 += y + "-"
        final += [s2[:-1]]
        s2 = ""
    return final

