"""


Create a function that returns the sum of missing numbers from the given list.

### Examples

    sum_missing_numbers([4, 3, 8, 1, 2]) ➞ 18
    # 5 + 6 + 7 = 18
    
    sum_missing_numbers([17, 16, 15, 10, 11, 12]) ➞ 27
    # 13 + 14 = 27
    
    sum_missing_numbers([1, 2, 3, 4, 5]) ➞ 0
    # No Missing Numbers (i.e. all numbers in [1, 5] are present in the list)

### Notes

The numerical range to consider when searching for the missing numbers in the
list is the sequence of consecutive numbers between the minimum and maximum of
the numbers (inclusive).

"""

def sum_missing_numbers(lst):
    summa = 0
    maximum = max(lst)+1
​
    minimum = min(lst)
​
    for i in range(minimum, maximum):        
        summa += i
    print(summa)
    for item in lst:
        summa -= item
    
    return summa

