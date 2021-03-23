"""


A **Fibonacci word** is a specific sequence of binary digits (or symbols from
any two-letter alphabet). The Fibonacci word is formed via _repeated
concatenation_ in the same fashion that the Fibonacci numbers are formed via
_repeated addition_.

Create a function that takes a number `n` as an argument and returns the first
`n` elements of the Fibonacci word sequence.

### Examples

    generate_word(1) ➞ "invalid"
    # if n < 2 then return "invalid".
    
    generate_word(3) ➞ "b, a, ab"
    
    generate_word(7) ➞ "b, a, ab, aba, abaab, abaababa, abaababaabaab"

### Notes

  * You are expected to solve this challenge via recursion.
  * You can check on the **Resources** tab for more details about recursion. 
  * A non-recursive version of this challenge can be found [here.](https://edabit.com/challenge/MiCMj8HvevYzGSb8J)

"""

def generate_word(n):
​
    def let_fib(seq1, seq2, num):
        if num == 0:
            return []
        lst = [seq1+seq2]
        lst.extend(let_fib(seq2, seq1+seq2, num-1))
        return lst
​
    if n < 2:
        return 'invalid'
    elif n == 2:
        return 'b, a'
    lst = ['b', 'a']
    lst.extend(let_fib('b', 'a', n-2))
    return ', '.join(lst)

