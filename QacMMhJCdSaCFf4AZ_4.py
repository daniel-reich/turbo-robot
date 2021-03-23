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
    a_a, c_a = seq[1] - seq[0], 2 * seq[0] - seq[1]
    a_g, c_g = seq[1] / seq[0], seq[0] * seq[0] / seq[1]
​
    def seq_a(n):
        return a_a * n + c_a
​
    def seq_g(n):
        return round(pow(a_g, n) * c_g)
​
    if seq_a(3) == seq[2] and seq_a(4) == seq[3] and seq_a(5) == seq[4]:
        return seq_a
    elif seq_g(3) == seq[2] and seq_g(4) == seq[3] and seq_g(5) == seq[4]:
        return seq_g

