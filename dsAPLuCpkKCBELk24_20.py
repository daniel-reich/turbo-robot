"""


You have a list of integers, and for each index you want to find the product
of every integer **except the integer at that index**.

Create a function that takes a list of integers and returns a list of the
products.

### Examples

    get_products([1, 7, 3, 4]) ➞ [84, 12, 28, 21]
    
    get_products([1, 7, 3, 4]) ➞ [84, 12, 28, 21]
    
    get_products([1, 2, 3, 0, 5]) ➞ [0, 0, 0, 30, 0]

### Notes

You can't use division, otherwise you might end up dividing by 0 and the
universe would end.

"""

def get_products(lst):
    result = []
    for i in lst:
        lst2 = lst[0:]
        lst2.remove(i)
        total, count = lst2[0], 0
        while count < len(lst2) - 1:
            total = total * lst2[count+1]
            count += 1
        result.append(total)
    return result

