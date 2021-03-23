"""


Create a function that takes a number and returns one digit that is the result
of summing all the digits of the input number. When the sum of the digits
consists of more than one digit, repeat summing until you get one digit.

### Examples

    root_digit(123) ➞ 6
    # 1 + 2 + 3 = 6
    
    root_digit(999888777) ➞ 9
    
    root_digit(1238763636555555555555) ➞ 6

### Notes

Recursion is allowed.

"""

def root_digit(num):
 if int(num)<10:
   return num
 else:
    num=str(num)
    list1=[]
    for i in num:
      list1.append(int(i))
    return sum(list1) if sum(list1)<9 else root_digit(sum(list1))

