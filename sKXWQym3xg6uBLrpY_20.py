"""


The median of a data sample is the value that separates the higher half and
the lower half of the data. For example, the median of `[1, 2, 3]` is `2`, and
the median of `[1, 2, 3, 4]` is `2.5` (because (2 + 3) / 2 = 2.5). Another way
of saying "median" is to say "Q2" (it's the second quartile). Q1 and Q3 are
the medians of the values above or below the Q2. The IQR is equal to Q3 - Q1.
Here's an example:

Let's say your data sample is: 1, 2, 3, 4

  * The median (Q2) is: (2+3)/2 =2.5
  * The lower half is: 1, 2
  * The upper half is: 3, 4
  * Q1 (median of the first half): (1+2)/2 = 1.5
  * Q3 (median of the second half): (3+4)/2 = 3.5
  * IQR = Q3 - Q1 = 3.5 - 1.5 = 2

If the length of the data sample is odd, as in: 1, 2, 3, 4, 5

  * The median (Q2) is: 3 (the number is in the middle, so no need to average).
  * 3 is the number that separates the upper and lower data, so we exclude it.
  * The lower half is: 1, 2
  * The upper half is: 4, 5
  * Q1 (median of the first half): (1+2)/2 = 1.5
  * Q3 (median of the second half): (4+5)/2 = 4.5
  * IQR = Q3 - Q1 = 4.5 - 1.5 = 3

For a more detailed explanation, please check the **Resources** tab.

Make a function that takes a list of floats and/or integers and returns the
IQR for that list. The return type can be `float` or `int`. It doesn't matter.

### Examples

    iqr([1, 2, 3, 4]) ➞ 2.0
    
    iqr([5, 4, 3, 2, 1]) ➞ 3.0
    
    iqr([-3.1, -3.8, -14, 23, 0]) ➞ 20.4

### Notes

  * In all test cases, none of the solutions have repeating decimals, so you shouldn't need to worry about rounding the result.
  * There is no universal agreement on how to select quartile values, so if you use an online calculator (such as Wolfram Alpha), you could get a different result depending on how the quartile values were calculated. You need to obtain the quartile values in the way described in the description, which is taken from the description given on khanacademy.com (see the **Resources** tab).

"""

def iqr(lst):
  lst.sort()
  if len(lst)%2 == 0:
    if len(lst)%4 == 0:
      hlv = int(len(lst)/2)
      st = int((len(lst)/4)-1)
      q1so = slice(st,st+2)
      q1 =sum(lst[q1so])/2
      q3so = slice(st+hlv,st+2+hlv)
      q3 = sum(lst[q3so])/2
    else:
      hlv = int(len(lst)/2)
      st = int((len(lst)/4))
      q1so = slice(st,st+1)
      q1 = sum(lst[q1so])
      q3so = slice(st+hlv,st+hlv+1)
      q3 = sum(lst[q3so])
  elif (len(lst)+1)%4 == 0:
    hlv = int(len(lst)/2)
    st = int((len(lst)/4))
    q1so = slice(st,st+1)
    q1 = sum(lst[q1so])
    q3so = slice(st+hlv+1,st+hlv+2)
    q3 = sum(lst[q3so])
  else:
    hlv = int(len(lst)/2)
    st = int((len(lst)/4)-1)
    q1so = slice(st,st+2)
    q1 = sum(lst[q1so])/2
    q3so = slice(st+hlv+1,st+3+hlv)
    q3 = sum(lst[q3so])/2
  return (q3-q1)

