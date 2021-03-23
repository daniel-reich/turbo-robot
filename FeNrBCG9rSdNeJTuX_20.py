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

def num_length(n):
    k = 0
    while n:
        k += 1
        n //= 10
    return k
​
def swap_digit(a, d, p):
    def helper(a, d, p, c, k):
        if p == 0:
            return (a // 10 * 10  + d) * k + c
        return helper(a // 10, d, p - 1, c + k * (a % 10), k * 10)
    return helper(a, d, p, 0, 1)
​
def maximizer(a, b):
    if not b:
        return a
    swap_combos = [a] + [swap_digit(a, b % 10, i) for i in range(0, num_length(a))]
    swap_combos = [maximizer(o, b // 10) for o in swap_combos]
    return max(swap_combos)
​
def max_possible(n1, n2):
  return maximizer(n1, n2)

