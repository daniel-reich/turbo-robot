"""


A number `n` becomes a super- _d_ number when, for any digit `d` from 2 up to
9, the result of `d * nᵈ` contains `d` consecutive digits equal to `d`.

Given a positive integer `n`, implement a function that returns:

  * `"Super-d Number"` if `n` is a super- _d_ number, replacing the letter `d` with the digit (any from 2 up to 9) that makes it super;
  * `"Normal Number"` if `n` is not a super- _d_ number.

### Examples

    is_super_d(19) ➞ "Super-2 Number"
    # when d = 2
    # 2 * 19² = 722
    # There are two (d) consecutives digits equal to 2 (d)
    
    is_super_d(753) ➞ "Super-3 Number"
    # when d = 3
    # 3 * 753³ = 1280873331
    # There are three (d) consecutives digits equal to 3 (d)
    
    is_super_d(1168) ➞ "Super-4 Number"
    # when d = 4
    # 4 * 1168⁴ = 7444428488704
    # There are four (d) consecutives digits equal to 4 (d)
    
    is_super_d(24) ➞ "Normal Number"
    # No cases where d * 24ᵈ (with d being any digit from 2 up to 9)...
    # ...leads to a result containing d consecutive digits equal to d

### Notes

Any given `n` will be a positive integer greater or equal to 0.

"""

def is_super_d(n):
 # for d = 2 to 9 incl.
 for d in range(2,10):
  # create prod
  prod=d*(n**d)
  # check if prod has d consecutive d's
  count=0
  prod_str=str(prod)
  i=0
  while count < d and i < len(prod_str):
   if int(prod_str[i]) == d:
    count+=1
   else:
    count=0
   i+=1
  # print('count',count)
  # if yes, return d - else "Normal Number" 
  if count == d:
   return "Super-"+str(d)+" Number"
 if count == 0:
  return "Normal Number"

