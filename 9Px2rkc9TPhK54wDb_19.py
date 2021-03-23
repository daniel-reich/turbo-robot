"""


In the ECG Sequence (that always starts with the numbers 1 and 2), every
number that succeeds is the smallest not already present in the sequence and
that shares a factor (excluding 1) with its preceding number. Every number in
the ECG Sequence (besides 1 and 2) has a different index from its natural
index in a normal numeric sequence. See the example below to establish the ECG
Sequence Index of number 3.

    # Find the smallest number that is not in sequence...
    # This number shares a factor with the preceding?
    
    SEQUENCE = [1, 2]
    
    3 = no factors shared with 2
    4 = shares factor 2 with number 2
    
    SEQUENCE = [1, 2, 4]
    
    3 = no factors shared with 4
    5 = no factors shared with 4
    6 = shares factor 2 with number 4
    
    SEQUENCE = [1, 2, 4, 6]
    
    3 = shares factor 3 with number 6
    
    SEQUENCE = [1, 2, 4, 6, 3]
    
    Number 3 is at index 4 in the ECG Sequence.

Given an integer `n` implement a function that returns its ECG Sequence Index.

### Examples

    ecg_seq_index(3) ➞ 4
    
    ecg_seq_index(5) ➞ 9
    
    ecg_seq_index(7) ➞ 13

### Notes

  * ECG is the acronym for the electrocardiogram: if you try to graphically represent the trend of the sequence, a similar scheme appears.
  * Curiosity: every odd prime `p` in the sequence is preceded by `2p` and followed by `3p`.

"""

import itertools
​
def factors(n):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n
​
seq = [1, 2]
queue = list(range(3, 1000))
last_factors = set(factors(seq[-1]))
while len(queue) > 0:
    idx = 0
    while True:
        cur = queue[idx]
        cur_factors = set(factors(cur))
        if len(last_factors.intersection(cur_factors)) > 0:
            # number found
            break
        idx += 1
        if idx >= len(queue):
            break
    if idx >= len(queue):
        break
    queue.pop(idx)
    seq.append(cur)
    last_factors = cur_factors  
​
def ecg_seq_index(n):
    return seq.index(n)

