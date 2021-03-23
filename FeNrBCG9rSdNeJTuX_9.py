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
    n2_img = sorted(str(n2), reverse = True)
    n1_img = list(str(n1))
    for j, c in enumerate(n2_img):
        for i, h in enumerate(n1_img):
            if int(c) > int(h):
                n1_img[i] = n2_img[j]
                break
    return int(''.join(n1_img))

