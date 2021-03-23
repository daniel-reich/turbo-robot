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
    if lst == []:
        return []
    result = []
    lst.sort()
    sublist = [lst[0]]
    for i in range(0,len(lst)):
        if i != 0:
            if lst[i]-1 == sublist[-1]:
                sublist.append(lst[i])
            else:
                if len(sublist) == 1:
                    result.append(str(sublist[0]))
                else:
                    result.append(str(sublist[0])+"-"+str(sublist[-1]))
                sublist = [lst[i]]
    if len(sublist) == 1:
        result.append(str(sublist[0]))
    else:
        result.append(str(sublist[0])+"-"+str(sublist[-1]))
    return result

