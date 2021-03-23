"""


The **Ulam sequence** starts with:

    ulam = [1, 2]

The next number in the sequence is the smallest positive number that is equal
to the _sum of 2 distinct numbers_ (that are already in the sequence) _exactly
one way_. Trivially, this is 3, as there are only 2 numbers in the starting
sequence.

    ulam = [1, 2, 3]

The next number is 4, which is the sum of 3+1. 4 is also 2+2, but this
equation does not count, as the 2 addends have to be distinct.

    ulam = [1, 2, 3, 4]

The next number _cannot be_ 5, as 5 = 1 + 4, but also 5 = 2 + 3. There should
only be one way to make an Ulam number from 2 distinct addends found in the
sequence. The next number is 6 (2+4). There are 2 ways to make 7 (1+6 or 3+4),
so the next is 8 (2+6). And so on.

    ulam = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, …]

Create a function that takes a number n and returns the nth number in the Ulam
sequence.

### Examples

    ulam(4) ➞ 4
    
    ulam(9) ➞ 16
    
    ulam(206) ➞ 1856

### Notes

N/A

"""

def ulam(n):
    lst = [1, 2]
    num = 3
    while len(lst) < n:
        count = 0
        for i in lst:
            if 2 * i > num and num - i in lst:
                count += 1
            if count > 1:
                break
        if count == 1:
            lst.append(num)
        num += 1
    return lst[-1]

