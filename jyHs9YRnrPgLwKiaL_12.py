"""


Before you start, please try the first part of this challenge: [Split 25 (Part
#1)](https://edabit.com/challenge/XjgoXNmnz59txiQp3)

After you completed the first part, you may have realized you could go higher
by not using natural numbers. You could use negatives and positives,
eventually reaching infinity, like so: `-25 * 25 * 50 * -25` so on and so on
continuing to add more factors. You could also use fractions and irrational
numbers to increase it.

Being in the interest of not overcomplicating this part, attempt to find the
highest product using fractions. For example, 10 could be broken up as `2.5 *
2.5 * 2.5 * 2.5` (which is (10/4)^4)and you could reach 39.0625, higher then
36 (3 _3_ 4).

Given a positive integer to split, x, return the maximum product using
rational numbers.

### Examples

    split(25) ➞ 9846.4
    # (25 / 9) ** 9
    
    split(15) ➞ 244.1
    # (15 / 6) ** 6
    
    split(1) ➞ 1

### Notes

All responses should be rounded to one decimal place.

"""

def power_divide(a,b):
  return round((a/b)**b,1)
​
def split(x):
  def power_divide(y):
    return round((x/y)**y,1)
  n = 1
  while power_divide(n+1) > power_divide(n):
    n += 1
  return power_divide(n)

