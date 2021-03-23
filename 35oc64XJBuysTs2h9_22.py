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

def mediane(l):
    l.sort()
    mod = (len(l)%2)
    if mod == 1:
        #median is the len(l)%2)th element
        median = l[int(len(l)/2)]
    else:
        #median is between the (len(l)%2)th element and the (len(l)%2 -1)th element
        median = (l[int(len(l)/2)]+l[int(len(l)/2)-1])/2.0
    return [[e for e in l[:int(len(l)/2)]] , [e for e in l[int(len(l)/2)+mod:]]], median
​
def turkey(lst):
    lst.sort()
    Q0 = lst[0]
    Q4 = lst[-1]
    halfed,Q2 = mediane(lst)
    if len(lst)%2 == 1:
        #odd situation, turkey method inculdes the median into upper && lower brackets
        halfed[0].reverse()
        halfed[0].append(Q2)
        halfed[0].reverse()
        halfed[1].append(Q2)
    Q1 = mediane(halfed[0])[1]
    Q3 = mediane(halfed[1])[1]
    return [Q0,Q1,Q2,Q3,Q4]
​
def MM(lst):
    lst.sort()
    Q0 = lst[0]
    Q4 = lst[-1]
    halfed,Q2 = mediane(lst)
    Q1 = mediane(halfed[0])[1]
    Q3 = mediane(halfed[1])[1]
    return [Q0,Q1,Q2,Q3,Q4]
​
def MS(lst):
    lst.sort()
    Q0 = lst[0]
    Q4 = lst[-1]
    Q2 = mediane(lst)[1]
    inc_Q1 = (len(lst)+1)/4
    inc_Q3  = inc_Q1*3
    if inc_Q1-float(int(inc_Q1))>=0.5:
        inc_Q1 = int(inc_Q1) +1
    else:
        inc_Q1 = int(inc_Q1)
​
    if inc_Q3-float(int(inc_Q3))>0.5:
        inc_Q3 = int(inc_Q3) +1
    else:
        inc_Q3 = int(inc_Q3)
    return [Q0,lst[inc_Q1-1],Q2,lst[inc_Q3-1],Q4]
​
​
def get_quartiles(lst,method):
    if method == 'T':
        return turkey(lst)
    if method =='MM':
        return MM(lst)
    if method == 'MS':
        return MS(lst)

