"""


Comparing two numbers written in index form like `2^11` and `3^7` is not
difficult, as any calculator would confirm that `2^11 = 2048 < 3^7 = 2187`.
However, confirming that `632382^518061 > 519432^525806` would be much more
difficult, as both numbers contain over three million digits.

Create a function that takes **Base-Exponent** pairs and returns the line
number which has the greatest numerical value.

### Examples

    largest_exponential([
      (519432,525806),
      (632382,518061),
      (78864,613712),
      (466580,530130),
      (780495,510032)
    ]) ➞ 5
    
    largest_exponential([
      (375856,539061),
      (768907,510590),
      (165993,575715),
      (976327,501755),
      (898500,504795),
      (360404,540830)
    ]) ➞ 4
    
    largest_exponential([
      (478714,529095),
      (694144,514472)
    ]) ➞ 1

### Notes

As mentioned, the actual values may contain some millions of digits. So, it's
impractical to actually calculate the values and compare them.

"""

def largest_exponential(values):
    '''
    Each number in the values list is a (num, exponential) pair. This function
    returns the index (from 1) of the number with the highest value.
    '''
    from math import log
​
    log_vals = [b * log(a,10) for a,b in values]
    return log_vals.index(max(log_vals)) + 1

