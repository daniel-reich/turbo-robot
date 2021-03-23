"""


Given a number, find the "round "of each digit of the number. An integer is
called "round" if all its digits except the leftmost (most significant) are
equal to zero.

  * Round numbers: 4000, 1, 9, 800, 90
  * Not round numbers: 110, 707, 222, 1001

Create a function that takes a number and returns the "round" of each digit
(except if the digit is zero) as a string. Check out the following examples
for more clarification.

### Examples

    sum_round(101) ➞ "1 100"
    
    sum_round(1234) ➞ "4 30 200 1000"
    
    sum_round(54210) ➞ "10 200 4000 50000"

### Notes

N/A

"""

def sum_round(num):
  A=[str(num)[i]+'0'*(len(str(num))-i-1) for i in range(len(str(num)))]
  A=[x for x in A if not all(y=='0' for y in x)]
  return ' '.join(A[::-1])
