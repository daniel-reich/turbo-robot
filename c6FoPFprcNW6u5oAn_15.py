"""


The Farey sequence of order `n` is the set of all fractions with a denominator
between 1 and `n`, reduced and returned in ascending order. Given `n`, return
the Farey sequence as a list, with each fraction being represented by a string
in the form "numerator/denominator".

### Examples

    farey(1) ➞ ["0/1", "1/1"]
    
    farey(4) ➞ ["0/1", "1/4", "1/3", "1/2", "2/3", "3/4", "1/1"]
    
    farey(5) ➞ ["0/1", "1/5", "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "1/1"]

### Notes

The Farey sequence will always begin with "0/1" and end with "1/1".

"""

def farey(n):
    lst = [str(i)+'/'+str(j) for i in range(0, n+1) for j in range(1, n+1) if i%j != 0 and i/j < 1]
    aux  = []
    for i in lst:
        if eval(i) not in aux:
            aux.append(eval(i))
            aux.append(i)
    aux = [i for i in aux if isinstance(i, str) == True]
    aux_eval = sorted([eval(i) for i in aux])
    res = ['0/1'] + [j for i in aux_eval for j in aux if eval(j) ==  i] + ['1/1']
    return res

