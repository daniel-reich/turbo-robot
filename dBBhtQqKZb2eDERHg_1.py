"""


Write a **recursive** function that accepts an integer `n` and return a
sequence of `n` integers as a string, descending from `n` to 1 and then
ascending back from 1 to `n` as in the examples below:

### Examples

    number_sequence(1) ➞ "1"
    
    number_sequence(2) ➞ "1 1"
    
    number_sequence(3) ➞ "2 1 2"
    
    number_sequence(4) ➞ "2 1 1 2"
    
    number_sequence(9) ➞ "5 4 3 2 1 2 3 4 5"
    
    number_sequence(10) ➞ "5 4 3 2 1 1 2 3 4 5"

### Notes

  * Only use recursion.
  * No auxiliary data structures like list and tuple are allowed.

"""

def numberSequence(n, seq=""):
    if n <= 0:
        return "-1"
    if seq == "":
        if n == 1:
            return "1"
        if n == 2:
            return "1 1"
        if n % 2 == 0:
            seq = "1 1"
            return numberSequence(n, seq)
        else:
            seq = "1"
            return numberSequence(n, seq)
    l = len(seq.split())
    if l == n:
        return seq.strip()
    last = int(seq.split()[-1])
    seq = str(last + 1) + ' ' + seq + ' ' + str(last + 1)
    return numberSequence(n, seq)

