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
    lista = [i * n for i in range(1, 2000000)]
    lista2 = sorted(list(zip([abs(num - i) for i in lista], lista)))
    if lista2[0][0] == lista2[1][0]:
        return max(lista2[0][1], lista2[1][1])
    else:
        return lista2[0][1]
​
​
# not proud

