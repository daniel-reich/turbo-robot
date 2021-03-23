"""


A leap year has one day added to February for being synchronized with the
seasonal year. A leap year appears with a regular frequency, which is
determined by the rule below:

  * A year must **either** be divisible by 400 **or** divisible by 4 **and not** 100.

Given a `year` you must implement a function that returns `True` if it's a
leap year, or `False` if it's not.

### Examples

    is_leap(2020) ➞ True
    # Exactly divided by 4 and not by 100.
    
    is_leap(1800) ➞ False
    # Exactly divided by 4, but is also exactly divided by 100.
    
    is_leap(2000) ➞ True
    # Exactly divided by 400.
    
    is_leap(2019) ➞ False
    # It can't be exactly divided by 400 or by 4.

### Notes

  *  _Exactly divided_ can be interpreted as _the remainder of the division is equal to 0_.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.
  * Bonus: Try to implement this function writing a single line of code.

"""

def is_leap(year):
  return year%400 == 0 or (year%4 == 0 and year%100 != 0)

