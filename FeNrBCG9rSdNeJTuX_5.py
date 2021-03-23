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
    n1 = [int(d) for d in str(n1)]
    n2 = sorted([int(d) for d in str(n2)], reverse=True)
    for i1, d1 in enumerate(n1):
        for i2, d2 in enumerate(n2):
            if d2 > d1:
                n1[i1] = n2.pop(i2)
                break
    return int(''.join(map(str, n1)))

