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
  answer=[f[0],f[1]]
  for i in range(n-2):
    answer.append(answer[-1]+answer[-2])
  return ', '.join(answer)

