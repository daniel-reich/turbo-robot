"""


A number is said to be Disarium if the **sum** of its _digits raised to their
respective positions_ is the number itself.

Create a function that determines whether a number is a Disarium or not.

### Examples

    is_disarium(75) ➞ False
    # 7^1 + 5^2 = 7 + 25 = 32
    
    is_disarium(135) ➞ True
    # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
    
    is_disarium(544) ➞ False
    
    is_disarium(518) ➞ True
    
    is_disarium(466) ➞ False
    
    is_disarium(8) ➞ True

### Notes

  * Position of the digit is 1-indexed.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/aifM22oGtRKShsFWB).

"""

def is_disarium(n):
    sum = 0
    digits_lst = []
    digit_dict = dict()
    for i in str(n):
        digits_lst.append(i.split())
    for j in range(len(digits_lst)):
        for k in range(len(digits_lst[j])):
            digit_dict[j + 1] = int(digits_lst[j][k])
    for key, value in digit_dict.items():
        sum += value ** key
    if sum == n :
        return True
    return False    
    
print(is_disarium(518))

