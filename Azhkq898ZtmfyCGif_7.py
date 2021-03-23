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
    
    rangeIdx=0
    
    if lst==[]:
        return []
    
    else:
        ranges=[[lst[0],lst[0]]]
        for i in lst:
            if ranges[rangeIdx][1] in (i,i-1):
                ranges[rangeIdx][1]=i
            else:
                ranges.append([i,i])
                rangeIdx+=1
    return (','.join(map(lambda p:'%s-%s'%tuple(p) if p[0]!=p[1] else str(p[0]),ranges ))).split(',')

