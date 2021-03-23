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

def max_possible(n1, n2):
    n1_str_list = list(str(n1))
    n2_str = str(n2)
​
    n2_str_sorted = sorted(n2_str, reverse=True)
​
    i = 0
    j = 0
    while i < len(n1_str_list) and j < len(n2_str_sorted):
        if int(n1_str_list[i]) < int(n2_str_sorted[j]):
            n1_str_list[i] = n2_str_sorted[j]
            j = j + 1
        i = i + 1
​
    return int(''.join(n1_str_list))

