"""


Create a function that counts number of palindromes within two timestamps
inclusive. A palindrome is a timestamp that can be read the same from left to
right and from right to left (e.g. `02:11:20`).

### Examples

    palindrome_time([2, 12, 22, 4, 35, 10]) ➞ 14
    
    palindrome_time([12, 12, 12, 13, 13, 13]) ➞ 6
    
    palindrome_time([6, 33, 15, 9, 55, 10]) ➞ 0

### Notes

Input list contains six numbers `[h1, m1, s1, h2, m2, s2]` for begin and end
timestamps.

"""

from datetime import datetime as dt, timedelta as td
def palindrome_time(lst):
    h1, m1, s1, h2, m2, s2 = lst
    t1 = dt(year=2020, month=1, day=1, hour=h1, minute=m1, second=s1)
    t2 = dt(year=2020, month=1, day=1, hour=h2, minute=m2, second=s2)
    one_sec, p_count = td(seconds=1), 0
    t1 -= one_sec
    while t1 < t2:
        t1 += one_sec
        str_t1 = dt.strftime(t1, '%H:%M:%S')
        str_tr = ''.join([c for c in str_t1][::-1])
        p_count += int(str_t1 == str_tr)
    return p_count

