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

def number_pairs(txt):
    txt  = txt.split(' ')
    numLis =  txt[1:]
    pair = 0
    while len(numLis):
        count = numLis.count(numLis[0])
        pair += count//2
        numLis = list(filter(lambda n: n !=numLis[0], numLis))
    return pair

