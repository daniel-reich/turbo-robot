"""


Write a function that takes in a string representation of an integer or
decimal number and returns the number of significant figures in the number.

Significant figures are an important part of science because they provide an
easy way to show the precision of a measurement at a glance. In general, the
more significant figures a number has, the more precise the measurement.

Significant figures are calculated by looking at the digits of a number and
determining the total number of digits that are "significant". The rules for
deciding which digits are significant are as follows:

  * Non-zero digits are significant.
  * `0`'s in between non-zero digits (from any distance) are significant.
  * Leading `0`'s (those to the left of all non-zero digits) are **not** significant.
  * Trailing `0`'s (those to the right of all non-zero digits) are significant **_only_** if the number contains a decimal point `.`.
  * If the entire number is equal to 0, return 0 for the number of significant figures.
  * Negative signs have no effect on the number of significant figures.

### Examples

    sig_figs("15030") ➞ 4
    
    sig_figs("0.0067") ➞ 2
    
    sig_figs("-290.00") ➞ 5
    
    sig_figs("-8080.") ➞ 4

### Notes

  * Each input consists of the digits 0-9, along with up to one decimal point `.` and/or negative sign `-`.
  * Just because two numbers are equal doen't mean that their number of sig figs are equal. For example, `1.02` has 3 sig figs while `1.020` has 4.
  * The function should correctly handle numbers that begin with a decimal point.
  * You might find regex helpful for this problem.

"""

import re
def sig_figs(num):
  add = '' if '.' in num else '[1-9]'
  meh = re.findall('^[1-9]$|[1-9]\d*{}'.format(add), re.sub('\.','',num))
  return len(meh[0]) if meh else 0

