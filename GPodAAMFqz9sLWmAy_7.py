"""


Given a **two digit** number, return `True` if that number contains **one
even** and **one odd** digit.

### Examples

    one_odd_one_even(12) ➞ True
    
    one_odd_one_even(55) ➞ False
    
    one_odd_one_even(22) ➞ False

### Notes

N/A

"""

def one_odd_one_even(n):
 k = str(n)
 s = [int(i) for i in k]
 if (s[0]%2==0 and s[1]%2 !=0) or ( s[0]%2!=0 and s[1]%2 ==0):
  return True
 else:
   return False

