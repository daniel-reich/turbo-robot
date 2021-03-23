"""


Create a function to generate all nonconsecutive binary strings where
nonconsecutive is defined as a string where no consecutive ones are present,
and where `n` governs the length of each binary string.

### Examples

    generate_nonconsecutive(1) ➞ "0 1"
    
    generate_nonconsecutive(2) ➞ "00 01 10"
    
    generate_nonconsecutive(3) ➞ "000 001 010 100 101"
    
    generate_nonconsecutive(4) ➞ "0000 0001 0010 0100 0101 1000 1001 1010"

### Notes

N/A

"""

def countStrings(n):
    x=[]
    x.append(0)
    p = (1 << n)
    for i in range(1, p):
        if ((i & (i << 1)) == 0):
            x.append(i)
    return x        
def generate_nonconsecutive(n):
    res,c='',n
    for i in countStrings(n):
        a=bin(i).replace('b','')
        if len(a)<c:
            b='0'*(c-len(a))
            a=b+a
        d=len(a)-c
        res+=a[d:]+' '
    return res.strip()

