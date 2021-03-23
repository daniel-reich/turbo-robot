"""


About a month ago I stumbled upon an interesting problem — something called
the 25 split. In the problem, you had to break up 25 into parts that add to
it, and, from those parts, try to create the biggest product.

For example, `3 * 22 = 66` or `5 * 5 * 5 * 5 * 5 = 3125`. With this first
part, return the value of the biggest product possible using natural number
parts from a given number, _x_.

### Examples

    split(5) ➞ 6
    # 3 times 2
    
    split(10) ➞ 36
    # 3 * 3 * 4
    
    split(1) ➞ 1

### Notes

  * 3's are useful...
  * Part 2 of this challenge is [here](https://edabit.com/challenge/jyHs9YRnrPgLwKiaL).

"""

def split(number):
  x = number
  twos = 0
  threes = 0
  fours = 0
  while x > 1:
    if x > 4 or x==3:
      x = x-3
      threes = threes + 1
    elif x == 4:
      x = x-4
      fours = fours + 1
    elif x == 2: 
      x = x-2
      twos = twos + 1
  return (2**twos)*(3**threes)*(4**fours)

