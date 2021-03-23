"""


Write a function that makes the **first number as large as possible** by
swapping out its digits for digits in the second number.

To illustrate:

    max_possible(9328, 456) ➞ 9658
    # 9658 is the largest possible number built from swaps from 456.
    # 3 replaced with 6 and 2 replaced with 5.

### Examples

    max_possible(523, 76) ➞ 763
    
    max_possible(9132, 5564) ➞ 9655
    
    max_possible(8732, 91255) ➞ 9755

### Notes

  * Each digit in the second number can only be used once.
  * Zero to all digits in the second number may be used.

"""

def max_possible(num, digits):
    num_list = [int(x) for x in str(num)]
    digits_list = [int(x) for x in str(digits)]
    digits_list.sort()
    digits_list = digits_list[::-1]
    for n in range(0,len(num_list)):
        if len(digits_list) > 0 and num_list[n] < digits_list[0]:
            num_list[n] = digits_list.pop(0)
    num_list = [str(x) for x in num_list]
    return int("".join(num_list))

