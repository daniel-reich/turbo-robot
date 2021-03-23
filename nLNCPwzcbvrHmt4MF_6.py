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

def fibonacciSequence():
  a = 0
  b = 1
  c = 0
  sequence = [0, 1,]
  while not b == 233:
    c = b + a
    sequence.append(c)
    ###
    a = c + b
    sequence.append(a)
    ###
    b = a + c
    sequence.append(b)
  return sequence

