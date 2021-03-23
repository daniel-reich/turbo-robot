"""


Given a list of numbers, create a function that removes 25% from every number
in the list except the smallest number, and adds the total amount removed to
the smallest number.

### Examples

    show_the_love([4, 1, 4]) ➞ [3, 3, 3]
    
    show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]
    
    show_the_love([2, 100]) ➞ [27, 75]

### Notes

There will only be one smallest number in a given list.

"""

def show_the_love(lst):
    total = 0
    smallest = lst[0]
    new_list = []
    
    for num in lst:
        rem = num * 0.25
        total += rem
        num -= rem
        new_list.append(num)
    
    lowest = min(new_list)
    index = new_list.index(lowest)
    new_list[index] += total
    
    return new_list

