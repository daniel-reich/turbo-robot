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
    t1 = [int(i) for i in str(n1)]
    t2 = [int(i) for i in str(n2)]
    for j in t1:
        for i in t2:
            try:
                if j < max(t2):
                    t1[t1.index(j)] = max(t2)
                    del t2[t2.index(max(t2))]
            except:
                pass
​
    return int(''.join([str(i) for i in t1]))

