"""


Given an integer, return `"odd"` if the sum of all _odd_ digits is greater
than the sum of all _even_ digits. Return `"even"` if the sum of _even_ digits
is greater than the sum of _odd_ digits, and `"equal"` if both sums are the
same.

### Examples

    odds_vs_evens(97428) ➞ "odd"
    # odd = 16 (9+7)
    # even = 14 (4+2+8)
    
    odds_vs_evens(81961) ➞ "even"
    # odd = 11 (1+9+1)
    # even = 14 (8+6)
    
    odds_vs_evens(54870) ➞ "equal"
    # odd = 12 (5+7)
    # even = 12 (4+8+0)

### Notes

N/A

"""

def odds_vs_evens(num):
    evensum = 0
    oddsum = 0
    oddlist = []
    evenlist = []
    result = 'unknown'
    num = str(num)
    for digit in num:
        if digit in {'1', '3', '5', '7', '9'}:
            oddlist.append(digit)
        else:
            evenlist.append(digit)
​
    for item in oddlist:
        oddsum += int(item)
​
    for item in evenlist:
        evensum += int(item)
​
    if oddsum > evensum:
        result = "odd"
    elif evensum > oddsum:
        result = "even"
    else:
        result = "equal"
​
    return result

