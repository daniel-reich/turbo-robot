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

def changeBase(num,b):
    ans = ''
    for i in range(20,-1,-1):
        z = num // b**i
        ans += str(num // b**i)
        num -= z * b**i
​
    return int(ans)
​
def esthetic(num):
    myans = []
    for i in range(2,11):
        t = str(changeBase(num,i))
        works = True
        for j in range(len(t)-1):
            if abs(int(t[j])-int(t[j+1])) != 1:
                works = False
                break
        if works:
            myans.append(i)
    if len(myans) > 0:
        return myans
    else:
        return 'Anti-Esthetic'

