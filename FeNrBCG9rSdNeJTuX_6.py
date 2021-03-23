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
  n1 = [int(x) for x in str(n1)] 
  n2 = [int(x) for x in str(n2)] 
​
  for i, num in enumerate(n1):
    if num < max(n2):
      j = n2.index(max(n2))
      n1[i] = n2[j]
      n2[j] = 0
      
  vysledok = 0
  i = 0
  
  n1.reverse()
  
  for x in n1:
    vysledok = vysledok + x*10**i
    i += 1
    
  return vysledok

