"""


Two consecutive integers `a` and `b` are considered a **Ruth-Aaron pair** if
the sum of the prime factors of `a` is equal to the sum of the prime factors
of `b`.

Two definitions exist:

  1. Summing up _distinct_ prime factors. For example, 24 and 25 constitute a Ruth-Aaron pair by this definition. 8 and 9 do not.

    P24 = [2, 3]  # sum = 5
    
    P25 = [5]  # sum = 5, equal to 24
    
    P8 = [2]  # sum = 2
    
    P9 = [3]  # sum = 3

  2. Summing up _repeated_ prime factors. By this definition, 24 and 25 do _not_ constitute a Ruth-Aaron pair. But 8 and 9 do.

    P24 = [2, 2, 2, 3]  # sum = 9
    
    P25 = [5, 5]  # sum = 10
    
    P8 = [2, 2, 2]  # sum = 6
    
    P9 = [3, 3]  # sum = 6, equal to 8

If two consecutive numbers have only distinct prime factors and have equal
sums of prime factors, they are considered Ruth-Aaron pairs by both
definitions.

    P77 = [7, 11]  # sum = 18
    
    P78 = [2, 3, 13]  # sum = 18

Create a function that takes a number `n` and returns:

  1. `False` if it is not part of a Ruth-Aaron pair.
  2. A 2-element list if it is part of a Ruth-Aaron pair.
    * The first element should be "Ruth" if `n` is the smaller number in the pair, or "Aaron" if it is the larger.
    * The second element should be 1 if `n` is part of a Ruth-Aaron pair under the first definition (sum of _distinct_ prime factors), 2 if it qualifies by the second definition, 3 if it qualifies under both.

### Examples

    ruth_aaron(5) ➞ ["Ruth", 3]
    
    ruth_aaron(25) ➞ ["Aaron", 1]
    
    ruth_aaron(9) ➞ ["Aaron", 2]
    
    ruth_aaron(11) ➞ False

### Notes

N/A

"""

def ruth_aaron(n):
  aaron, ruth, product, sums, ab, ac = False, False, False, False, False, False
  a_p, b_p, c_p = summ(n), summ(n+1), summ(n-1)
  if sum(a_p) == sum(b_p): sums, ab = True, True
  if sum(a_p) == sum(c_p): sums, ac = True, True
  alp, blp, clp = prods(n), prods(n+1), prods(n-1)
  if  sum(alp) == sum(blp): product, ab = True, True
  if sum(alp) == sum(clp): product, ac = True, True
  if ab: ruth, aaron = True, False
  if ac: aaron, ruth = True, False
  name =  "Aaron" if aaron else "Ruth" if ruth else 0 
  if name == 0: return False
  return [name, 3 if product and sums else 2 if product else 1]
  
  
  
def prods(y):
  ret = []
  x = 2
  while not prime(y):
    while y % x == 0: 
      ret.append(x)
      y = y// x
    x += 1
  if y > 1: ret.append(y)
  return ret
  
def summ(y):
  return [ x for x in range(2, y+1) if y % x == 0 and prime(x)]
  
def prime(n):
  return len([x for x in range(2, n//2+1) if n % x == 0]) == 0

