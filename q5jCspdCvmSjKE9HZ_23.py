"""


Create a function that takes a list of more than three numbers and returns the
**Least Common Multiple** (LCM).

### Examples

    lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 2520
    
    lcm_of_list([13, 6, 17, 18, 19, 20, 37]) ➞ 27965340
    
    lcm_of_list([44, 64, 12, 17, 65]) ➞ 2333760

### Notes

The LCM of a list of numbers is the smallest positive number that is divisible
by each of the numbers in the list.

"""

def lcm_of_list(numbers):
    lcm_1 = 1
    for i in range(len(numbers)):
        lcm_num = findlcm(lcm_1, numbers[i])
        lcm_1 = lcm_num
    return(lcm_1)
    
    
def findlcm(a, b):   # Function definition
    if(a > b):   
        maximum = a
    else:
        maximum = b
    while(True):
        if(maximum % a == 0 and maximum % b == 0):
            lcm = maximum;
            break;
        maximum = maximum + 1
    return lcm

