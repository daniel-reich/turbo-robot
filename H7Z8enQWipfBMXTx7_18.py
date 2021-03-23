"""


A Fibonacci string is a precedence of the Fibonacci series. It works with any
two characters of the English alphabet (as opposed to the numbers `0` and `1`
in the Fibonacci series) as the initial items and concatenates them together
as it progresses similarly to that of the Fibonacci series.

### Examples

    fib_str(3, ["j", "h"]) ➞ "j, h, hj"
    
    fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"
    
    fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"

### Notes

  * All values for `n` will be at least 2.
  * It is expected from the challenge-takers to come up with a solution using the concept of **recursion** or the so-called **recursive approach**.
  * You can read more topics about recursion (see **Resources** tab) if you aren't familiar with it yet or hasn't fully understood the concept behind it before taking up this challenge or unless otherwise.
  * A non-recursive version of this challenge can be found in [here](https://edabit.com/challenge/kozqCJFi4de2JnR26).

"""

def fib_str(n, f):
    f1=f
    x=[]
    x.append(f[0])
    x.append(f[1])
    f=sorted(f)
    if f1!=f:
        a=f[0]
        b=f[1]
        f[1]=f1[1]
    print(f,f1)
    c=a+b
    d=f[1]
    n=n-3
    x.append(c)
    for _ in range(n):
        m=c+d
        x.append(m)
        d=c
        c=m        
    return ', '.join(x)

