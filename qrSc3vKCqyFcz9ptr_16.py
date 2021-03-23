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
  a = []
  for i, j in enumerate(str(num)[::-1]):
      if j!="0":
         a.append(j+i*"0")
  return " ".join(a)
