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
  def test(n, d):
​
    tnum = str(d * n**d)
​
    count = 0
    consecuative = False
​
    for n in range(0, len(tnum)):
​
      item = tnum[n]
​
      i = int(item)
​
      if i == d:
        if consecuative == False:
          count += 1
          consecuative = True
        elif consecuative == True:
          count += 1
          if count == d:
            return True
      if i != d:
        if consecuative == True:
          consecuative = False
          count = 0
    
    return False
  
  tests = []
​
  for num in range(2, 10):
​
    t = test(n, num)
​
    if t == True:
      return 'Super-{d} Number'.format(d = num)
    
  return "Normal Number"

