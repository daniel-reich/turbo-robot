"""


The golden ratio is ubiquitous in math, science, art, and nature. This
challenge is concerned with the number itself, which is 1.618033988 to 10
significant digits. Implement a function that calculates the golden ratio to
100 significant digits using only integers, strings and basic arithmetic
operations: `+`, `-`, `*`, `//`

### Examples

    golden_ratio() ➞ 1.618033988+90 more decimal places

### Notes

This function has no argument so naturally there is only one test case.

"""

def golden_ratio():
    s=i=0
    while len(str(s))<100:
        r=0
        i+=1
        s=int(str(s)+str(i))
        while int(str(r)[0])<5:
            r=s*s
            s+=1
        s-=2
        i=0
    gr=int(str(int(str(s)[0])+1)+str(s)[1:])//2
    return str(gr)[0]+'.'+str(gr)[1:]

