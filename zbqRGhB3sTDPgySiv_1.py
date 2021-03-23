"""


Modify the inefficient code in the **Code** tab so it can pass the tests.

### Examples

    mod(1, 1) ➞ 0
    
    mod(5, 5) ➞ 34
    
    mod(13, 27 ) ➞ 522956314
    
    mod(8000, 30) ➞ 9157958657951075573395300940314

### Notes

  * The variables will be natural numbers.
  * If necessary, there is a hint in the **Tests** tab.

"""

def mod(base, key):
    fact, loop = [1], 0
    for i in range(1, key+1):fact+=[fact[-1]*i]
    for i in range(base):
      if i<key:loop+=fact[i]
      elif i!=key:
        r = (fact[-1]*i%fact[-1])%fact[-1]
        if r:fact+=[r]
        loop+=fact[-1]
    return loop % fact[key]

