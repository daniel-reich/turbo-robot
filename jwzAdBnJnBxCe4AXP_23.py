"""


Given a number, return the **difference** between the maximum and minimum
numbers that can be formed when the digits are rearranged.

### Examples

    rearranged_difference(972882) ➞ 760833
    # 988722 - 227889 = 760833
    
    rearranged_difference(3320707) ➞ 7709823
    # 7733200 - 23377 = 7709823
    
    rearranged_difference(90010) ➞ 90981
    # 91000 - 19 = 90981

### Notes

N/A

"""

def rearranged_difference(num):
    upper = sorted(list(str(num)),reverse=True)
    lower = sorted(list(str(num)))
​
    upper_int = int(''.join(upper).lstrip('0'))
    lower_int = int(''.join(lower).lstrip('0'))
​
    return upper_int - lower_int
