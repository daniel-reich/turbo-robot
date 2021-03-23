"""


Write a function that takes an integer `i` and returns an integer with the
integer backwards followed by the original integer.

To illustrate:

    123

We reverse `123` to get `321` and then add `123` to the end, resulting in
`321123`.

### Examples

    reverse_and_not(123) ➞ 321123
    
    reverse_and_not(152) ➞ 251152
    
    reverse_and_not(123456789) ➞ 987654321123456789

### Notes

`i` is a non-negative integer.

"""

reverse_and_not=lambda i:int(str(i)[::-1]+str(i))

