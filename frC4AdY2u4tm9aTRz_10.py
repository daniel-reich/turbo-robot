"""


The _central tendency measures_ ( _mean_ , _mode_ and _median_ ) sometimes
aren't enough descriptives in a data set analysis. For example, given two
lists `A=[15, 15, 15, 14, 16]` and `B=[2, 7, 14, 22, 30]` the mean is `μ=15`
in both cases, however the values of second list are clearly more spread out
from the average value. The **standard deviation** (also called _**sigma**_ ,
the greek lowercase letter _**σ**_ ) **measures the spread of the values in a
data set** and transform the _"clearly more spread out than"_ assertion in a
proofed statistical assertion. You can find more information in the
**Resources** tab.

The standard deviation is calculated following five steps:

  1. Obtain the mean of the data set.
  2. For each value in the set calculate the absolute difference between the value and the mean.
  3. Square each value obtained and sum them cumulatively.
  4. Divide the result by the data set length.
  5. Get the square root of the value obtained.

Given a list of values return the standard deviation rounded to the nearest
hundredth.

### Examples

    standard_deviation([3, 5, 7]) ➞ 1.63
    // |(3-5)|+|(5-5)|+|(7-5)| = 2² + 0 + 2² = 8 / 3 = square root of 2.66 = 1.63
    
    standard_deviation([5, 5, 5]) ➞ 0
    // Values aren't deviating from the mean.
    
    standard_deviation([-3, -5, -7]) ➞ 1.63
    // Remember: absolute differences!

### Notes

  * All given lists are valid, no exceptions to handle.
  * Lists can contain either positive or negative integers.
  * Remember to round to the nearest hundredth at the end.

"""

def standard_deviation(lst):
  mean = sum(lst) / len(lst)
  diffs = [abs(mean - i) for i in lst]
  return round((sum(i**2 for i in diffs) / len(lst)) ** 0.5, 2)

