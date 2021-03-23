"""


The Fibonacci Sequence is the sequence of numbers (Fibonacci Numbers) whose
sum is the two preceding numbers (e.g. 0, 1, 1, 2, 3, etc). Using 0 and 1 as
the starting values, create a function that returns a list containing all of
the Fibonacci numbers less than 255.

### Examples

On generating a Fibonacci number where input is the two preceding values
starting from 0 and 1 `[0, 1, ...]`.

    fibonacci_sequence(0, 1) ➞ 1
    
    fibonacci_sequence(1, 1) ➞ 2
    
    fibonacci_sequence(1, 2) ➞ 3

### Notes

N/A

"""

def fibonacci_sequence():
  L = [0, 1]
  while L[-1] + L[-2] < 255:
    L.append(L[-1] + L[-2])
  return L

