"""


Create a function that returns the **integral** part from the result of a
division between two numbers. This process of division can be achieved via
**repetitive subtraction** , thus, it can be done **recursively**.

### Examples

    divide(10, 2) ➞ 5
    
    divide(-51, -4) ➞ 12
    
    divide(3, 9) ➞ 0
    
    divide(-21, 5) ➞ -4
    
    divide(1024, 7) ➞ 146
    
    divide(273, -6) ➞ -45

### Notes

  * There will be no **zero-values** for the _divisor_.
  * You're expected to solve this challenge using a **recursive approach**.
  * You can read on more topics about recursion (see **Resources** tab) if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge.

"""

def divide(dividend, divisor):
    neg = 1
    if dividend < 0 and divisor < 0:
        dividend *= -1
        divisor *= -1
    elif dividend < 0 or divisor <0:
        neg = -1
        if dividend < 0:
            dividend *= -1
        else:
            divisor *= -1
    if dividend < divisor:
        return 0
    return neg*(1 + divide(dividend-divisor, divisor))

