"""


Create a function that takes an integer list and return the biggest between
**positive** sum, **negative** sum, or **0s** count. The major is understood
as the greatest absolute.

`l = [1,2,3,4,0,0,-3,-2]`, the function has to return `10`, because:

  * Positive sum = 1+2+3+4 = 10
  * Negative sum = (-3)+(-2) = -5
  * 0s count = 2 (there are two zeros in list)

### Examples

    major_sum([1, 2, 3, 4, 0, 0, -3, -2]) ➞ 10
    
    major_sum([-4, -8, -12, -3, 4, 7, 1, 3, 0, 0, 0, 0]) ➞ -27
    
    major_sum([0, 0, 0, 0, 0, 1, 2, -3]) ➞ 5
    # Because -3 < 1+2 < 0sCount = 5

### Notes

  * All numbers are integers.
  * There aren't empty lists.
  * All tests are made to return only one value.

"""

def major_sum(lst):
  positive=sum([i for i in lst if i>0])
  negative=sum([i for i in lst if i<0])
  zero=len([i for i in lst if i==0])
  large=max(positive,abs(negative),zero)
  if large==abs(negative):
    return negative
  else:
    return large

