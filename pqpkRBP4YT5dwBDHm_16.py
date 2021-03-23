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
    indx = lst.index(min(lst))
    value = lst[lst.index(min(lst))];sm=0
    for i,a in enumerate(lst):
        if i==indx:
            continue
        else:
            lst[i]=lst[i]-a/4
            sm+=a/4
    lst[indx] = value + sm
    return lst

