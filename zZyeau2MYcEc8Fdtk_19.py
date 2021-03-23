"""


Create a function that takes two integers, `num` and `n`, and returns an
integer which is divisible by `n` and is the closest to `num`. If there are
two numbers equidistant from `num` and divisible by `n`, select the larger
one.

### Examples

    round_number(33, 25) ➞ 25
    
    round_number(46, 7) ➞ 49
    
    round_number(133, 14) ➞ 140

### Notes

`n` will always be a positive number.

"""

def round_number(num, n):
    inc = num; dec = num; res = []
​
    while inc % n != 0:
        inc += 1
    else:
        res.append(inc)
    
    while dec % n != 0:
        dec -= 1
    else:
        res.append(dec)
​
    dif = []
    for i in res:
        dif.append(abs(i-num))
​
    min_dif = min(dif)
​
    end = []
    for i in range(len(dif)):
        if dif[i] == min_dif:
            end.append(res[i])
​
    return max(end)

