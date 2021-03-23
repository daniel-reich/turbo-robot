"""


Write a function that takes an integer sequence represented by a list of
integers as a parameter and return a function of that sequence. This function
should take an index (starting at 1, **not zero** ), and return the sequence
term at that index.

The test sequences given will have at least five terms and will start at the
beginning of the sequence. They will be either arithmetic or geometric
sequences of the following forms:

#### Arithmetic:

    f(n) = a*n + c

#### Geometric:

    f(n) = a^n * c

### Examples:

    sequence_generator([1, 2, 3, 4, 5])(3) ➞ 3
    
    sequence_generator([2, 4, 6, 8, 10, 12])(7) ➞ 14
    
    sequence_generator([2, 4, 8, 16, 32, 64])(4) ➞ 16

### Notes

N/A

"""

def sequence_generator(seq):
    d1, d2 = seq[1] - seq[0], seq[2] - seq[1]
    if d1 == d2:
        # arithmetic
        a = d1
        c = seq[0] - a
        return lambda n: a * n + c 
    # geometric
    a = d2 // d1
    c = seq[0] // a
    return lambda n: c * a**n

