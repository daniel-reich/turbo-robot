"""


Create a function that determines how many number pairs are there embedded in
a space-separated string. The first numeric value in the space-separated
string represents the count of the numbers, thus, excluded in the pairings.

### Examples

    number_pairs("7 1 2 1 2 1 3 2") ➞ 2
    # (1, 1), (2, 2)
    
    number_pairs("9 10 20 20 10 10 30 50 10 20") ➞ 3
    # (10, 10), (20, 20), (10, 10)
    
    number_pairs("4 2 3 4 1") ➞ 0
    # although two 4's are present but
    # the first one is discounted

### Notes

Always take into consideration the first number in the string is not part of
the pairing, thus, the count. It may not seem so useful as most people see it,
but it's mathematically significant if you deal with **set operations**.

"""

def number_pairs(t):
    v, p, p1, r, t = [i +" " for i in t.split()[1:]], set(), -1, 0, t+" "
    for i in v:
        p1 = t.find(i, p1 + 1)
        p2 = t.find(i, p1 + 1)
        if p2 > p1 and {p1, p2}.intersection(p)==set():
            p.update([p1, p2])
            r += 1
    return r

