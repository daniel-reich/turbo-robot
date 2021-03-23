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

import math
def get_quartiles(lst, method):
    lst.sort()
    l = len(lst)
    if method == 'T' or 'MM':
        q1 = median(lst[:l//2+1]) if l%2 and method == 'T' else median(lst[:l//2])
        q3 = median(lst[l//2+1:]) if l%2 and method == 'MM' else median(lst[l//2:])
    if method == 'MS':
        i = (l+1)/4
        n1 = round(i) if (l-1) % 4 else math.ceil(i)
        n3 = round(3*i) if (l-1) % 4 else math.floor(3*i)
        q1, q3 = lst[n1-1], lst[n3-1]
    return [lst[0],q1, median(lst), q3, lst[-1]]
​
​
def median(lst):
    l = len(lst)
    return lst[l//2] if l%2 else sum(lst[l//2-1: l//2+1])/2

