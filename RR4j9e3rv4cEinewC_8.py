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
    target, lines = lst
    if target == 1:
        minutes = min(lines)
        return '{} minutes'.format(minutes) if minutes > 1 else '1 minute'
    num, den = 0, 1
    for i in range(len(lines)):
        product = 1
        for j in range(len(lines)):
            if j != i:
                product *= lines[j]
        num += product
        den *= lines[i]
    minutes = int(target * den / num)
    n_cycles = minutes // min(lines)
    minutes = n_cycles * min(lines)
    n_hats = sum(minutes // line for line in lines)
    while n_hats < target:
        minutes += 1
        n_hats = sum(minutes // line for line in lines)
    return '{} minutes'.format(minutes) if n_hats == target else None

