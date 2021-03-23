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

def lowestnum(x=list):
    lowest=x[0]
    for y in x:
        if y<lowest:
            lowest=y
    return lowest
# now we assign the lowest number in the list in the function
def show_the_love(lst=list):
    a=lowestnum(lst)
    f=0
    for number in lst:
        if number!=a:
            b=number*(3/4)
            c=lst.index(number)
            lst.remove(number)
            lst.insert(c,b)
            f+=number*(1/4)
    d=lst.index(a)
    lst.remove(a)
    lst.insert(d,f+a)
    return lst

