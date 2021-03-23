"""


Create a function that takes a number `num` and returns its length.

### Examples

    number_length(10) ➞ 2
    
    number_length(5000) ➞ 4
    
    number_length(0) ➞ 1

### Notes

 **The use of the len() function is prohibited.**

"""

def number_length(num):
    if num == 0:
        return 1
    cnt = 0
    while num > 0:
        num = num // 10
        cnt += 1
    return cnt

