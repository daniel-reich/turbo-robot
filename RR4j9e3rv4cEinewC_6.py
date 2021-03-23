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

def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def lcm(a, b):
    return (a * b) // gcd(a, b)
​
def hats(lst):
    n, prod = lst
    l = lcm(lcm(lcm(lcm(prod[0], prod[1]), prod[2]), prod[3]), prod[4])
    time = 0
    all_even = sum([l // prod[i] for i in range(5)])
    while n >= all_even:
        n -= all_even
        time += l
    while n > 0:
        time += 1
        for i in range(5):
            r = time / prod[i]
            if time >= prod[i] and abs(r - int(r)) < 1e-4:
                n -= 1
    if n == 0:
        return "1 minute" if time == 1 else str(time) + " minutes"

