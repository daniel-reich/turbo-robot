"""


A number is Esthetic if, in any base from `base2` up to `base10`, the absolute
difference between every pair of its adjacent digits is constantly equal to
`1`.

    num = 441 (base10)
    # Adjacent pairs of digits:
    # |4, 4|, |4, 1|
    # The absolute difference is not constant
    # 441 is not Esthetic in base10
    
    441 in base4 = 12321
    # Adjacent pairs of digits:
    # |1, 2|, |2, 3|, |3, 2|, |2, 1|
    # The absolute difference is constant and is equal to 1
    # 441 is Esthetic in base4

Given a positive integer `num`, implement a function that returns a list
containing the bases (as integers from 2 up to 10) in which `num` results to
be Esthetic, or a string `"Anti-Esthetic"` if no base makes `num` Esthetic.

### Examples

    esthetic(10) ➞ [2, 3, 8, 10]
    # 10 in base2 = 1010
    # 10 in base3 = 101
    # 10 in base8 = 12
    # 10 in base10 = 10
    
    esthetic(23) ➞ [3, 5, 7, 10]
    # 23 in base3 = 212
    # 23 in base5 = 43
    # 23 in base7 = 32
    # 23 in base10 = 23
    
    esthetic(666) ➞ [8]
    # 666 in base8 = 1232

### Notes

N/A

"""

VALUES = {chr(65+i): 10+i for i in range(26)}
for i in range(10):
    VALUES[str(i)] = i
INV_VALUES = {value: key for key, value in VALUES.items()}
​
POWERS = {(base, power): base**power for base in range(1, 37) for power in range(200)}
​
def to_base(d, to_base):
    # convert decimal integer (base 10) to base base_k
    res = ""
    for p in range(50, -1, -1):
        power = POWERS[(to_base, p)]
        m = d // power
        res += INV_VALUES[m]
        d = d % power
    while res[0] == '0':
        res = res[1:]
    return res
​
def esthetic(num):
    L = []
    for base in range(2, 11):
        n = to_base(num, base)
        #print(num, base, n)
        if all([abs(int(n[i]) - int(n[i-1])) == 1 for i in range(1, len(n))]):
            L.append(base)
    return L if len(L) > 0 else "Anti-Esthetic"

