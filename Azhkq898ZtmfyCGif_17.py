"""


Create a function which converts an **ordered** number list into a list of
ranges (represented as strings). Note how some lists have some numbers
missing.

### Examples

    numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]
    
    numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]
    
    numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]
    
    numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]

### Notes

  * If there are no numbers consecutive to a number in the list, represent it as only the _string_ version of that number (see example #4).
  * Return an empty list if the given list is empty.

"""

def numbers_to_ranges(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return ['{}'.format(lst[0])]
    begin = lst[0]
    res = []
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1] + 1 or i == len(lst) - 1:
            end = lst[i - 1] if i < len(lst) - 1 else lst[i]
            if end > begin:
                res.append('{}-{}'.format(begin, end))
            else:
                res.append('{}'.format(begin))
            begin = lst[i]
    return res
