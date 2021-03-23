"""


Create a function that takes two parameters (`start`, `stop`), and returns the
sum of all even numbers in the range.

### Examples

    sum_even_nums_in_range(10, 20) ➞ 90
    # 10, 12, 14, 16, 18, 20
    
    sum_even_nums_in_range(51, 150) ➞ 5050
    
    sum_even_nums_in_range(63, 97) ➞ 1360

### Notes

Remember that the `start` and `stop` values are inclusive.

"""

def sum_even_nums_in_range(start, stop):
    result = 0
    if not (start%2==0):
        start+=1
    for i in range(start, stop+1, 2):      
        result += i
    return result

