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

from itertools import permutations as pt
​
​
def is_vampire(n):
    if n < 100:
        return 'Normal Number'
    lst = list(pt(list(str(n))))
    len_n = len(str(n))
    half_len = len_n // 2
    product_equal = False
    for tpl in lst:
        left = int(''.join(tpl[i] for i in range(half_len)))
        right = int(''.join(tpl[i] for i in range(half_len, len_n)))
        if left * right == n:
            product_equal = True
    if len_n % 2 and product_equal:
        return 'Pseudovampire'
    elif product_equal:
        return 'True Vampire'
    else:
        return 'Normal Number'

