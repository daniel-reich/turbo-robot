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

is_arithmetic = lambda s : len(set(j-i for i,j in zip(s, s[1:]))) == 1
​
def sequence_generator(seq):
  if is_arithmetic(seq):
    return lambda n : seq[0] + (seq[1] - seq[0]) * (n - 1)
  else:
    return lambda n : seq[0] * (seq[1] / seq[0]) ** (n - 1)

