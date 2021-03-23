"""


The **digit distance** between two numbers is the total value of the
difference between each pair of digits.

To illustrate:

    digit_distance(234, 489) ➞ 12
    # Since |2 - 4| + |3 - 8| + |4 - 9| = 2 + 5 + 5

Create a function that returns the **digit distance** between two integers.

### Examples

    digit_distance(121, 599) ➞ 19
    
    digit_distance(12, 12) ➞ 0
    
    digit_distance(10, 20) ➞ 1

### Notes

  * Both integers will be exactly the same length.
  * All digits in `num2` have to be higher than their counterparts in `num1`.

"""

def digit_distance(num1, num2):
  s=0
  while num1>0 and num2>0:
    s+=abs(num1%10-num2%10)
    num1//=10
    num2//=10
  return s

