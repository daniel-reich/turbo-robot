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
  lst = []
  lst.append(0);
  lst.append(1);
  for i in range(2,number+1):
    m = i;
    for j in range(1,i):
      if (lst[j] * lst[i-j]) > m:
        m = lst[j] * lst[i-j];
    lst.append(m);
  return lst[number]

