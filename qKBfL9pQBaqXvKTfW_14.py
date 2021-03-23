"""


Create a function that takes a list as an argument and return a list of the
sum of each of its slices. A list's slices are groups of consecutive values
that add up to a maximum of 100. No slice's total sum should exceed 100.
However, if a single integer equals or exceeds 100, return the integer as
well.

### Examples

    sum_of_slices([10, 29, 13, 14, 15, 16, 17, 31, 20, 10, 29, 13, 14, 15, 16, 17, 31, 20, 100])
    ➞ [97, 78, 87, 68, 100]
    
    # First slice: [10, 29, 13, 14, 15, 16]
    # 10 + 29 + 13 + 14 + 15 + 16 = 97
    # The next value could not be included in this slice because
    # the total would exceed 100.
    
    # Second slice: [17, 31, 20, 10]
    # 17 + 31 + 20 + 10 = 78
    # The next value could not be included in this slice because
    # the total would exceed 100.
    
    # And so on ...
    sum_of_slices([58, 3, 38, 99, 10]) ➞ [99, 99, 10]
    
    sum_of_slices([13]) ➞ [13]

### Notes

Do not sort the list.

"""

def sum_of_slices(lst):
    lst_total=[]
    total=0
    for num in lst:
        if total+num<100:
            total+=num
        elif total+num>100:
            lst_total.append(total)
            total=num
        else:
            lst_total.append(100)
            total=0
        
    return lst_total +[total]

