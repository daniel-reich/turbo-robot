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
    n, lines = lst
    lo = n*(min(lines))//5-1
    hi = 10*(n+100)*min(lines)+50
    while hi-lo > 1:
        h = (hi+lo)//2
        if n > sum(h // l for l in lines):
            lo = h
        else:
            hi = h
    k = sum(hi // l for l in lines)
    return "{} minute{}".format(hi, 's' if hi > 1 else '') if n == k else None

