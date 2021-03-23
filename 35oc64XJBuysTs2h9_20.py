"""


In statistic a quartile is a type of _quantile_ , more specifically is any of
the three values (q1, q2 or q3) that divide the items of a sorted frequency
distribution (that starts at _q0_ with the lowest value and ends at _q4_ with
the highest value) into four classes with each containing one fourth of the
total population.

There are three main methods used for calculate the quartiles of a dataset:
**Tukey** ( _abbr._ **T** ), **Moore & McCabe** ( _abbr._ **MM** ) and
**Mendenhall & Sincich** ( _abbr._ **MS** ). (see **_Resources_** tab for more
informations about quartiles and other calculation methods).

  * As already said, in a dataset **q0 is the lowest value** and **q4 is the highest value**.
  * All methods share one common statement: **q2 is equal to the median of the set.**
  * Using T or MM you split the dataset in two parts:

    * If dataset has an odd population **T includes the median** appending it at the end of the lower half and at the beginning of the upper half, while **MM excludes the median** from both parts.
    * If dataset has an even population is splitted in two equal parts by both methods.
    * With the dataset split in two **q1 is equal to the median of the lower half** and **q3 is equal to the median of the upper half**.
  * Using MS you don't split the dataset:

    *  **q1 is equal to the nth term of the dataset** with n equal to `(population length + 1) / 4`, _rounded to the nearest integer_ , unless the decimal part is equal to `0.5`, in that case it should be _rounded **up** to the nearest integer_.
    *  **q3 is equal to the nth term of the dataset** with n equal to `3 * (population length + 1) / 4` _rounded to the nearest integer_ , unless the decimal part is equal to `0.5`, in that case it should be _rounded **down** to the nearest integer_.

Given a list of values and a string with one of the three possible methods
("T", "MM" or "MS") return a list in the form `[q0, q1, q2, q3, q4]`.

### Examples

    get_quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "T") ➞ [1, 3.5, 6, 8.5, 11]
    # T includes the median (q2 = 6) in lower half (1 to 6, q1 = mean of 3+4)
    # and in upper half (6 to 11, q3 = mean of 8+9).
    
    get_quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "MM") ➞ [1, 3, 6, 9, 11]
    # MM excludes the median in lower half (1 to 5, q1 = 3) and in upper
    # half (7 to 11, q3 = 9).
    
    get_quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9] ➞ [1, 3, 5, 7, 9]
    # With MS q1 = population + 1 = 11 / 4 = 2.75 rounded up to 3 = third
    # number of dataset, and q2 = population + 1 = 11 * 3 = 33 / 4 = 8.25
    # rounded down to 8 = eighth number of dataset.

### Notes

  * Try [this challenge](https://edabit.com/challenge/9tkmnkgWyxaWeRTNt) if you need to get familiar with medians.
  * The dataset has to be sorted in ascending order.
  * Values can be either positive or negative integers.
  * All given lists are valid, no exceptions to handle.

"""

def get_quartiles(lst, method):
  def Turkey(lst):
​
    q0 = min(lst)
    q4 = max(lst)
​
    lst = sorted(lst)
​
    if len(lst) % 2 == 0:
      
      n1index = int(len(lst)/2) - 1
      n2index = n1index + 1
​
      n1 = lst[n1index]
      n2 = lst[n2index]
​
      q2 = (n1 + n2) / 2
​
      lower = lst[:n2index]
      upper = lst[n2index:]
    else:
      
      mindex = int(len(lst) / 2) 
​
      q2 = lst[mindex]
      
      lower = list(lst[:mindex])
      lower.append(lst[mindex])
      upper = lst[mindex:]
​
    
    if len(lower) % 2 == 0:
      
      n1index = int(len(lower) / 2) - 1
      n2index = n1index + 1
​
      n1 = lower[n1index]
      n2 = lower[n2index]
​
      q1 = (n1 + n2) / 2
    else:
​
      mindex = int(len(lower) / 2)
​
      q1 = lower[mindex]
    
    if len(upper) % 2 == 0:
      
      n1index = int(len(upper) / 2) - 1
      n2index = n1index + 1
​
      n1 = upper[n1index]
      n2 = upper[n2index]
​
      q3 = (n1 + n2) / 2
    else:
​
      mindex = int(len(upper) / 2)
​
      q3 = upper[mindex]
    
    return [q0, q1, q2, q3, q4]
  def Moore_McCab(lst):
​
​
    q0 = min(lst)
    q4 = max(lst)
​
    lst = sorted(lst)
​
    if len(lst) % 2 == 0:
      
      n1index = int(len(lst)/2) - 1
      n2index = n1index + 1
​
      n1 = lst[n1index]
      n2 = lst[n2index]
​
      q2 = (n1 + n2) / 2
​
      lower = lst[:n2index]
      upper = lst[n2index:]
    else:
      
      mindex = int(len(lst) / 2) 
​
      q2 = lst[mindex]
      
      lower = list(lst[:mindex])
      upper = lst[mindex + 1:]
​
    
    if len(lower) % 2 == 0:
      
      n1index = int(len(lower) / 2) - 1
      n2index = n1index + 1
​
      n1 = lower[n1index]
      n2 = lower[n2index]
​
      q1 = (n1 + n2) / 2
    else:
​
      mindex = int(len(lower) / 2)
​
      q1 = lower[mindex]
    
    if len(upper) % 2 == 0:
      
      n1index = int(len(upper) / 2) - 1
      n2index = n1index + 1
​
      n1 = upper[n1index]
      n2 = upper[n2index]
​
      q3 = (n1 + n2) / 2
    else:
​
      mindex = int(len(upper) / 2)
​
      q3 = upper[mindex]
    
    return [q0, q1, q2, q3, q4]
  def Mendenhall_Sincich(lst):
​
    q0 = min(lst)
    q4 = max(lst)
​
    lst = sorted(lst)
​
    q1ri = (len(lst) + 1) / 4
​
    if q1ri - int(q1ri) >= .5:
      q1i = int(q1ri) + 1
    else:
      q1i = int(q1ri)
    
    q1 = lst[q1i - 1]
​
    if len(lst) % 2 == 0:
      
      n1index = int(len(lst)/2) - 1
      n2index = n1index + 1
​
      n1 = lst[n1index]
      n2 = lst[n2index]
​
      q2 = (n1 + n2) / 2
    else:
      
      mindex = int(len(lst) / 2) 
​
      q2 = lst[mindex]
    
    q3ri = 3 * q1ri
    if q3ri - int(q3ri) > .5:
      q3i = int(q3ri) + 1
    else:
      q3i = int(q3ri)
​
    q3 = lst[q3i - 1]
​
    return [q0, q1, q2, q3, q4]
​
  if method == 'T':
    return Turkey(lst)
  elif method == 'MM':
    return Moore_McCab(lst)
  elif method == 'MS':
    return Mendenhall_Sincich(lst)
  else:
    return 'Incorrect Method: {}'.format(method)

