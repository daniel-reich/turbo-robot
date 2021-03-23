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

def convert_base(n, base):
    b = 0
    b_list = []
    while True:
        power = base**b
        b += 1
        b_list.append(power)
        if power > n:
            break
    b_list.sort(reverse=True)
​
    answer = ''
    for i in b_list:
        x = n // i
        answer += str(x)
        if x > 0:
            n -= i*x
    return int(answer)
​
​
def is_Esthetic(n):
    c = 0
    n = str(n)
    for i in range(len(str(n))-1):
        if abs(int(n[i]) - int(n[i + 1])) == 1:
            c += 1
    if c == len(str(n))-1:
        return True
​
def esthetic(n):
    list_of_bases = []
    for i in range(2, 11):
        all_bases = convert_base(n, i)
        if is_Esthetic(all_bases):
            list_of_bases.append(i)
    if len(list_of_bases) > 0:
        return list_of_bases
    else:
        return 'Anti-Esthetic'

