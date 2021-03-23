"""


In a calendar year, it is exactly 365.25 days. But, eventually, this will lead
to confusion because humans normally count by exact divisibility of 1 and not
with decimal points. So, to avoid the latter, it was decided to add up all
0.25 days every four-year cycle, make that year to sum up to 366 days
(including February 29 as an intercalary day), thus, called a **leap year**
and aside the other years of the four-year cycle to sum up to 365 days, **not
a leap year**.

In this challenge, (though quite repetitive), we'll take it to a new level,
where, you are to determine if it's a leap year or not without the use of the
**datetime** class, **if blocks** , **if-elif blocks** , **conditionals** (`a
if b else c`) nor the logical operators **AND** (`and`) and **OR** (`or`) with
the exemption of the **NOT** (`not`) operator.

Return `True` if it's a leap year, `False` otherwise.

### Examples

    leap_year(1979) ➞ False
    
    leap_year(2000) ➞ True
    
    leap_year(2016) ➞ True
    
    leap_year(1521) ➞ False
    
    leap_year(1996) ➞ True
    
    leap_year(1800) ➞ False

### Notes

You can't use the **datetime** class, **if statements** in general, the
**conditional** nor the **logical operators** (`and`, `or`).

"""

def leap_year(yr):
    return yr in (list(filter(lambda y: y % 100, range(1000, 3000, 4))) + list(range(1200, 3000, 400)))

