"""


Consider the following operation on an arbitrary positive integer:

  * If `n` is even -> `n / 2`
  * If `n` is odd -> `n * 3 + 1`

Create a function to repeatedly evaluate these operations, until reaching 1.
Return the number of steps it took.

See the following example, using `10` as the input, with 6 steps:

  1. 10 is even - 10 / 2 = 5
  2. 5 is odd - 5 * 3 + 1 = 16
  3. 16 is even - 16 / 2 = 8
  4. 8 is even - 8 / 2 = 4
  5. 4 is even - 4 / 2 = 2
  6. 2 is even - 2 / 2 = 1 -> Reached 1, so return `6`

### Examples

    collatz(2) ➞ 1
    
    collatz(3) ➞ 7
    
    collatz(10) ➞ 6

### Notes

For further information, check the **Resources** tab.

"""

def collatz(num):
  new = [num // 2, num * 3 + 1][num % 2]
  return 0 if num == 1 else collatz(new) + 1

