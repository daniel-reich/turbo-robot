"""


Given any number, we can create a new number by **adding the sums of squares
of digits of that number**. For example, given `203`, our new number is `4 + 0
+ 9 = 13`. If we repeat this process, we get a sequence of numbers:

    203 -> 13 -> 10 -> 1 -> 1

Sometimes, like with `203`, the sequence reaches (and stays at) `1`. Numbers
like this are called **happy**.

Not all numbers are happy. If we started with `11`, the sequence would be:

    11 -> 2 -> 4 -> 16 -> ...

This sequence will never reach `1`, and so the number `11` is called
**unhappy**.

Given a positive whole number, you have to determine whether that number is
happy or unhappy.

### Examples

    happy(203) ➞ True
    
    happy(11) ➞ False
    
    happy(107) ➞ False

### Notes

  * You can assume _(and it is actually true!)_ that all positive whole numbers are either happy or unhappy. Any happy number will have a `1` in its sequence, and every unhappy number will have a `4` in its sequence.
  * The only numbers passed to your function will be positive whole numbers.

"""

def happy(n):
  for i in range(10):
    numbers = []
    while n>0:
      numbers.append(n%10)
      n = int(n/10)
    numbers = list(map(lambda x:x*x,numbers))
    n = sum(numbers)
  if n==1:
    return True
  else:
    return False

