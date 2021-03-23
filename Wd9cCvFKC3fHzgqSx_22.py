"""


Create a function that takes a number `num` and returns each place value in
the number.

### Examples

    num_split(39) ➞ [30, 9]
    
    num_split(-434) ➞ [-400, -30, -4]
    
    num_split(100) ➞ [100, 0, 0]

### Notes

N/A

"""

def num_split(num):
    if num < 0:
        return [int('-' + str(int(j)*10**int(len(str(num))-(i+2)))) for i,j in enumerate(str(abs(num)))]
    return [int(j)*10**int(len(str(num))-(i+1)) for i,j in enumerate(str(num))]

