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

def max_possible( n1, n2):
    l1 = list(map(int, list(str(n1))))
    l2 = sorted(map(int, list(str(n2))), reverse=True)
    lo = []
    for index in range(0, len(l1)):
        if not l2:
            lo.append(l1[index])
            continue
        if l2[0] > l1[index]:
            lo.append(l2.pop(0))
        else:
            lo.append(l1[index])
    no = lo[0]
    for index in range(1, len(lo)):
        no = no*10 + lo[index]
    return no

