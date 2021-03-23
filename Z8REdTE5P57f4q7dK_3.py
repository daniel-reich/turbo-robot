"""


A Collatz sequence is generated like this. Start with a positive number. If
it's even, halve it. If it's odd, multiply it by three and add one. Repeat the
process with the resulting number. The Collatz Conjecture is that every
sequence eventually reaches 1 (continuing past 1 just results in an endless
repeat of the sequence `4, 2, 1`).

The length of the sequence from starting number to 1 varies widely.

Create a function that takes a number as an argument and returns a tuple of
two elements — the number of steps in the Collatz sequence of the number, and
the highest number reached.

### Examples

    collatz(2) ➞ (2, 2)
    # seq = [2, 1]
    
    collatz(3) ➞ (8, 16)
    # seq = [3, 10, 5, 16, 8, 4, 2, 1]
    
    collatz(7) ➞ (17, 52)
    # seq = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    
    collatz(8) ➞ (4, 8)
    # seq = [8, 4, 2, 1]

### Notes

(Improbable) Bonus: Find a positive starting number that doesn't reach 1, and
score a place in Math history plus a cash prize.

"""

def collatz(n):
  steps = 1
  highnum = 0
  seq = [n]
​
  for i in seq:
    if i % 2 != 0 and i != 1:
      seq.append((i * 3) + 1)
      steps += 1
      if ((i * 3) + 1) > highnum:
        highnum = ((i * 3) + 1)
    elif i % 2 == 0:
      seq.append(i/2)
      steps += 1
      if (i / 2) > highnum:
        highnum = (i / 2)
    else:
      seq.append(1)
      break
  return (steps, int(highnum))

