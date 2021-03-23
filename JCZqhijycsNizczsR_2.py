"""


Given two arguments, return a list which contains these two arguments.

### Examples

    make_pair(1, 2) ➞ [1, 2]
    
    make_pair(51, 21) ➞ [51, 21]
    
    make_pair(512124, 215) ➞ [512124, 215]

### Notes

N/A

"""

make_pair = lambda *args: list(args)

