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
    # test arithmetic series:
    diffs = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    if len(set(diffs)) == 1:
        # it's a arithmetic series:
        a = diffs[0]
        c = seq[0] - a
        return lambda n: a * n + c
    else:
        # it's a geometric series:
        a = seq[1] // seq[0]
        c = seq[0]
        return lambda n: pow(a, n - 1) * c

