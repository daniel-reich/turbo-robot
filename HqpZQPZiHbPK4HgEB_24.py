"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

def at_most_one_swap_permutation(sequence):
    subject = list(sequence)
    for a in range(len(sequence) - 1):
        for b in range(a + 1, len(sequence)):
            subject[a], subject[b] = subject[b], subject[a]
            yield subject
            subject[a], subject[b] = subject[b], subject[a]
    yield subject
​
def max_and_min(iterable):
    iterable = iter(iterable)
    try:
        first = next(iterable)
    except StopIteration:
        raise ValueError("empty iterable") from None
    else:
        a_min, a_max = first, first
    for candidate in iterable:
        if candidate < a_min:
            a_min = candidate
        if candidate > a_max:
            a_max = candidate
    return a_max, a_min
​
def maxmin(number):
    return max_and_min(
        int(''.join(x))
        for x in at_most_one_swap_permutation(str(number))
        if x[0] != '0'
    )

