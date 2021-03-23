"""


This fabled hat company has 5 production lines running simultaneously. The
speed of each production line varies depending on the style and quality of the
hat being produced. You will be given the number of hats required and a list
of production line speeds.

Your job is to devise a function that will find the number of minutes elapsed
for exactly `n` hats to be finished. If exactly `n` hats cannot be made in any
time frame, return `None`. The speeds given are the number of minutes required
to make one hat.

### Examples

    hats([5, [1, 1, 1, 1, 1]]) ➞ "1 minute"
    # If each line makes a hat in 1 min, it takes 1 min to make 5 hats.
    
    hats([3, [23, 11, 19, 9, 36]]) ➞ "18 minutes"
    
    hats([650, [23, 11, 19, 9, 36]]) ➞ "2001 minutes"
    
    hats([9, [23, 11, 19, 9, 36]]) ➞ None

### Notes

N/A

"""

def hats(lst):
    cycle = []
    l = lcm(lst[1])
    for i in lst[1]:
        a = i
        cycle.append(i)
        while a < l:
            a += i
            cycle.append(a)
    cycle = sorted(cycle)
    n = lst[0]
    a, n = divmod(n, len(cycle))
    if n > 0:
        sol = cycle[n - 1]
    else:
        sol = 0
    e = ["s", ""][a * cycle[-1] + sol == 1]
    if sol != cycle[n] or sol == 0:
        return "{} minute{}".format((a * cycle[-1]) + sol, e) 
    return None
    
def lcm(x):
    f, r = {}, 1
    for i in x:
        d = get_factors(i)
        for j in set(d):
            f[j] = max(f.get(j, d.count(j)), d.count(j))
    for k in f:
        r *= k ** f[k]
    return r 
    
def get_factors(x):
    p = []
    i = 2
    while x > 1:
        if x % i == 0:
            p.append(i)
            x = x // i
            i = 2
        else:
            i += 1
    return p

