"""


A Vampire Number is a positive integer greater than 99, that rearranged in all
of its possible digits permutations, with every permutation being split into
two parts, is equal to the product of at least one of its permutations.

  * If the number has an even quantity of digits, left and right parts will have the same length in every permutation;
  * If the number has an odd quantity of digits and at least three digits, the left and right parts will present different lengths for every possible permutation, alternating between them in the range +1 and -1.

Given a positive integer `n`, implement a function that returns the type of
`n` as a string:

  * `'Normal Number'` if `n` is lower than 100 or if no permutations return a product of their parts equal to `n`.
  * `'Pseudovampire'` if `n` it is a Vampire with an odd quantity of digits.
  * `'True Vampire'` if `n` it is a Vampire with an even quantity of digits.

### Examples

    is_vampire(1260) ➞ "True Vampire"
    # Has an even number of digits and is greater than 99)
    # Permutations:
    # 12 * 60 = 720
    # 16 * 20 = 320
    # 10 * 26 = 260
    # 21 * 60 = 1260
    
    is_vampire(126) ➞ "Pseudovampire"
    # Has an odd number of digits and is greater than 99
    # Permutations:
    # 12 * 6 = 72
    # 1 * 26 = 26
    # 21 * 6 = 126
    
    is_vampire(67) ➞ "Normal Number"
    # Is lower than 100
    # Permutations:
    # 6 * 7 = 7 * 6 = 42

### Notes

Trivially, a number from 1 to 99 is a Normal Number by the definitions: a
single-digit number can't be split into two parts, and the product of the
permutated two digits of a number will always be lower than the number itself.

"""

from functools import reduce
from math import ceil, floor
​
def permuta(lst, step=0):
    if step==len(lst):
        return lst
    flst = []
    nlst = lst.copy()
    for i in range(step, len(nlst)):
        nlst[step],nlst[i] = nlst[i],nlst[step]
        b = list(permuta(nlst, step+1))
        if type(b)==list and type(b[0])==tuple:
            flst += b
        else:
            flst.append(b)
    flst = list(map(tuple, flst))
    return set(flst)
​
def p2(lst):
    lst = list(lst)
    if len(lst[0])%2==0:
        k = len(lst[0])//2
        nlst = [("".join(lst[i][:k]),"".join(lst[i][k:])) for i in range(len(lst))]
        return nlst
    else:
        top = ceil(len(lst[0])/2)
        btm = floor(len(lst[0])/2)
        nlst = [("".join(lst[i][:top]),"".join(lst[i][top:])) for i in range(len(lst))]
        nlst += [("".join(lst[i][:btm]),"".join(lst[i][btm:])) for i in range(len(lst))]
        return nlst
        
def is_vampire(number):
    if len(str(number))==1:
        return "Normal Number"
    lnum = [a for a in str(number)]
    ncomb = list(permuta(lnum))
    ncomb = p2(ncomb)
    for i in range(len(ncomb)):
        ncomb[i] = tuple(map(int, ncomb[i]))
    cv = checker(ncomb, number) 
    if cv == False:
        return "Normal Number"
    elif len(str(number))%2==0:
        return "True Vampire"
    else:
        return "Pseudovampire"
​
def checker(lst, number):
    if len(lst)==1:
        a = reduce(lambda x,y: x*y, lst[0])
        return a==number
    a = reduce(lambda x,y: x*y, lst[0])
    return a==number or checker(lst[1:], number)

