"""


This is a big integer challenge. You are given an integer which is a **perfect
square**. It is composed of 40 or more digits. Compose a function which will
find the exact square root of this integer.

### Examples

    square_root(152415787532388367501905199875019052100) ➞ 12345678901234567890
    
    square_root(10203040506070809101112131413121110090807060504030201) ➞ 101010101010101010101010101

### Notes

  * All test cases are perfect squares.
  * A **good fortune** bonus awaits you if you are able to complete this challenge without importing anything.

"""

def square_root(n):
    r=i=0
    digits=(len(str(n))+(len(str(n))%2==1))//2
    while r!=n:
        i*=10
        r=0
        while r<n:
            i+=1
            s=int(str(i)+'0'*(digits-len(str(i))))
            r=s*s
            if i%10==0:break
        i-=1
    return s

