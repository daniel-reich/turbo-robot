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

def split(n):
    '''
    Returns the biggest product for natural numbers (positive integers) whose
    sum equals n
    '''
    if n == 1:
        return 1
​
    pow3 = n // 3
    rem = n % 3
    if rem == 1:
        pow3 -= 1   # drop a power of 3
​
    return 3**pow3 * 2**((n-3*pow3)//2)

