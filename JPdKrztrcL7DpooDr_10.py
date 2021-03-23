"""


A Collatz sequence is generated by repeatedly applying the following rules to
an integer and then to each resulting integer in turn:

  * If even: divide by 2.
  * If odd: multiply by 3, then add 1.

The Collatz conjecture states that, for any initial positive integer, you will
eventually reach the number 1.

Write a function that, for an initial positive integer _n_ , returns a list
containing 2 values:

  1. The number of times the Collatz rule has to be applied until you reach 1.
  2. The maximum number reached in the process.

### Examples

    collatz(17) ➞ [12, 52]
    # Because 17 – 52 – 26 – 13 – 40 – 20 – 10 – 5 – 16 – 8 – 4 – 2 – 1
    # takes 12 steps and 52 is the highest number reached.
    
    collatz(6) ➞ [8, 16]
    
    collatz(21) ➞ [7, 64]

### Notes

N/A

"""

def collatz(n):
  num_steps = 0
  highest_number = n
  while n > 1:
    n = n / 2 if n % 2 == 0 else n*3 + 1
    highest_number = n if n > highest_number else highest_number
    num_steps += 1
  return [num_steps, highest_number]

