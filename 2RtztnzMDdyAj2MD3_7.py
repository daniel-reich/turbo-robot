"""


Create a function that takes two number strings and returns their sum as a
string.

### Examples

    add("111", "111") ➞ "222"
    
    add("10", "80") ➞ "90"
    
    add("", "20") ➞ "Invalid Operation"

### Notes

If any input is `""` or `None`, return `"Invalid Operation"`.

"""

add=lambda x,y:x and y and str(int(x)+int(y))or"Invalid Operation"

