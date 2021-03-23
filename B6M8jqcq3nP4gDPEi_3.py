"""


Write a function that extracts the max value of a number in a list. If there
are **two or more** max values, return it **as a list** , otherwise, return
the **number**. This process could be relatively easy with some of the built-
in list functions but the required approach is **recursive**.

### Examples

    iso_group([31, 7, 2, 13, 7, 9, 10, 13]) ➞ 31
    
    iso_group([1, 3, 9, 5, 1, 7, 9, -9]) ➞ [9, 9]
    
    iso_group([97, 19, -18, 97, 36, 23, -97]) ➞ [97, 97]
    
    iso_group([-31, -7, -13, -7, -9, -13]) ➞ [-7, -7]
    
    iso_group([-1, -3, -9, -5, -1, -7, -9, -9]) ➞ [-1, -1]
    
    iso_group([107, 19, -18, 79, 36, 23, 97]) ➞ 107

### Notes

You can read more about recursion (see the **Resources** tab) if you aren't
familiar with it yet or haven't fully understood the concept before taking up
this challenge.

"""

def iso_group(lst):
    '''
    Uses a recursive approach to return the maximum value(s) in lst as per
    the instructions
    '''
​
    def _iso_group(lst, biggest):
        '''
        Helper to iso_group - updates list biggest to that it contains
        the maximum value(s) in lst
        '''
        if len(lst) > 0:
            num = lst[0]
            if num > biggest[0]:
                 biggest = [num]
            elif num == biggest[0]:
                biggest.append(num)
            biggest = _iso_group(lst[1:], biggest)
​
        return biggest
​
    biggest = _iso_group(lst[1:], [lst[0]])
    return biggest if len(biggest) > 1 else biggest[0]

