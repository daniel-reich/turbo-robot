"""


A Fibonacci Word is a specific sequence of binary digits (or symbols from any
two-letter alphabet). The Fibonacci Word is formed by repeated concatenation
in the same way that the Fibonacci numbers are formed by repeated addition.

Create a function that takes a number `n` as an argument and returns the first
`n` elements of the Fibonacci Word sequence.

If `n < 2`, the function must return `"invalid"`.

### Examples

    fibo_word(1) ➞ "invalid"
    
    fibo_word(3) ➞ "b, a, ab"
    
    fibo_word(7) ➞ "b, a, ab, aba, abaab, abaababa, abaababaabaab"

### Notes

N/A

"""

def fibo_word(n):
    x='b' 
    y='a' 
    if n<2:
        return "invalid"
    lst=[]
    lst.append(x)
    lst.append(y)
    for i in range(n-2):
        tmp=y+x 
        lst.append(tmp)
        x=y
        y=tmp
    return ", ".join(lst)

