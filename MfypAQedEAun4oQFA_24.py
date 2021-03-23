"""


Each number in the _Perrin_ sequence is created by summing the numbers two
positions and three positions before it. The first three numbers are (3, 0,
2), and the sequence is extended as follows:

    P(0) P(1) P(2) P(3) P(4) P(5) P(6) P(7) ... P(n)
    3, 0, 2, 3, 2, 5, 5, 7, ...

Given a value for `n`, return the Perrin number P(n).

### Examples

    perrin(1) ➞ 0
    
    perrin(8) ➞ 10
    
    perrin(26) ➞ 1497

### Notes

Check the **Resources** tab for a further explanation of the Perrin sequence.

"""

def perrin(n):
    seq_perrin = []
​
    seq_perrin.append(3)
    seq_perrin.append(0)
    seq_perrin.append(2)
​
    if n == 2 or n==1 or n==0:
        return seq_perrin[n]
​
    if n > 2:
        for i in range(3, n + 1):
            seq_perrin.append(seq_perrin[i-2] + seq_perrin[i-3])
​
​
    return (seq_perrin[-1])

