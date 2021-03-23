"""


A Fibonacci string is a precedence of the Fibonacci series. It works with any
two characters of the English alphabet (as opposed to the numbers `0` and `1`
in the Fibonacci series) as the initial items and concatenates them together
as it progresses in a similar fashion as the Fibonacci series.

### Examples

    fib_str(3, ["j", "h"]) ➞ "j, h, hj"
    
    fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"
    
    fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"

### Notes

  * All values for `n` will be at least `2`.
  * A recursive version of the challenge can be found in [here](https://edabit.com/challenge/H7Z8enQWipfBMXTx7).

"""

def fib_str(n, txt):
  firstletter = txt[0]
  secondletter = txt[1]
  fib = {1: firstletter, 2: secondletter}
  for i in range(3,n+1):
    fib[i] = fib[i-1] + fib[i-2]
  emptystring = ''
  for eachkey in fib.keys():
    emptystring += fib[eachkey] + ', '
  return emptystring.strip()[:-1]

