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

def generate_word(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Parameters.append(["b","a"])
    
  Required = Parameters[0]
  Sequence = Parameters[1]
  
  if (Required < 2):
    return "invalid"
  
  elif (len(Sequence) >= Required):
    Link = ", "
    Answer = Link.join(Sequence)
    return Answer
  
  else:
    Upcoming = Sequence[-2] + Sequence[-1]
    Sequence.append(Upcoming)
    return generate_word(Required, Sequence)
