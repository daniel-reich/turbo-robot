"""


Create a function that takes a number as an argument and returns a string
formatted to separate thousands.

### Examples

    format_num(1000) ➞ "1,000"
    
    format_num(100000) ➞ "100,000"
    
    format_num(20) ➞ "20"

### Notes

You can expect a valid number for all test cases.

"""

def format_num(n):
    s_n = str(n)
    
    for i in range(len(s_n),0,-3):
        s_n = s_n[:i] + ',' + s_n[i:]
    
    return s_n[:len(s_n)-1]

