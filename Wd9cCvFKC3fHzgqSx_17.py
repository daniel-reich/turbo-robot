"""


Create a function that takes a number `num` and returns each place value in
the number.

### Examples

    num_split(39) ➞ [30, 9]
    
    num_split(-434) ➞ [-400, -30, -4]
    
    num_split(100) ➞ [100, 0, 0]

### Notes

N/A

"""

def num_split(n):
    lt=[]
    if n<0:
        n=str(n).lstrip("-")
        for x in range(len(str(n))):
            a=int(n)%10
            lt.append(-a*(10**x))
            n=int(n)//10
    else:
        for x in range(len(str(n))):
            a=n%10
            lt.append(a*(10**x))
            n=n//10
    return lt[::-1]

