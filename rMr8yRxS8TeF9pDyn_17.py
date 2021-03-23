"""


There's a great war between the even and odd numbers. Many numbers already
lost their life in this war and it's your task to end this. You have to
determine which group sums larger: the even, or the odd. The larger group
wins.

Create a function that takes a list of integers, sums the even and odd numbers
separately, then returns the difference between sum of even and odd numbers.

### Examples

    war_of_numbers([2, 8, 7, 5]) ➞ 2
    # 2 + 8 = 10
    # 7 + 5 = 12
    # 12 is larger than 10
    # So we return 12 - 10 = 2
    
    war_of_numbers([12, 90, 75]) ➞ 27
    
    war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168

### Notes

The given list contains only positive integers.

"""

def war_of_numbers(lst):
    sum_e=0
    sum_o=0
    for _ in lst:
        if(int(_)%2==0):
            sum_e+=_
        else:
            sum_o+=_
    if (sum_e>sum_o):
        return (sum_e-sum_o)
    else:
        return(sum_o-sum_e)

