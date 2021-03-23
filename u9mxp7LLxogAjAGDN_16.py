"""


A numbers **factor length** is simply its total number of factors.

For instance:

    3: 1, 3
    # 3's factor length = 2
    
    8: 1, 2, 4, 8
    # 8's factor length = 4
    
    36 : 1, 2, 3, 4, 6, 9, 12, 18, 36
    # 36's factor length = 9

Create a function that sorts a list by **factor length** in **descending
order**. If multiple numbers have the same factor length, sort these numbers
in **descending order** , with the largest first.

In the example below, since 13 and 7 both have only 2 factors, we put 13 ahead
of 7.

    factor_sort([9, 7, 13, 12]) ➞ [12, 9, 13, 7]
    # 12 : 6, 9: 3, 13: 2, 7: 2

### Examples

    factor_sort([1, 2, 31, 4]) ➞ [4, 31, 2, 1]
    
    factor_sort([5, 7, 9]) ➞ [9, 7, 5]
    
    factor_sort([15, 8, 2, 3]) ➞ [15, 8, 3, 2]

### Notes

Descending order: numbers with a higher factor length go before numbers with a
lower factor length.

"""

def factor_sort(nums):
    dic = {key : 0 for key in nums}
    for number in nums:
        dic[number] = len([d for d in range(1, number + 1) if number % d == 0])
    return [i[0] for i in sorted(dic.items(), key=lambda p : (p[1], p[0]), reverse=True)]

