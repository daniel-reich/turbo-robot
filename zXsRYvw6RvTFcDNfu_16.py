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

def ruth_aaron(a):
  arepeating = []
  anonrepeating = set()
  b = a
  while b != 1:
    for i in range(2, b + 1):
      if b % i == 0:
        factors = 0
        for j in range(2, i):
          if i % j == 0:
            factors += 1
        if factors == 0:
          arepeating.append(i)
          anonrepeating.add(i)
          b = int(b/i)
  arepeating.sort()
  arsum = 0
  anrsum = 0
  for i in arepeating:
    arsum += i
  for i in anonrepeating:
    anrsum += i
  result = []
  success = 0
  crepeating = []
  cnonrepeating = set()
  b = a -1
  while b != 1:
    for i in range(2, b + 1):
      if b % i == 0:
        factors = 0
        for j in range(2, i):
          if i % j == 0:
            factors += 1
        if factors == 0:
          crepeating.append(i)
          cnonrepeating.add(i)
          b = int(b/i)
  crepeating.sort()
  crsum = 0
  cnrsum = 0
  for i in crepeating:
    crsum += i
  for i in cnonrepeating:
    cnrsum += i
  if arsum == crsum and anrsum == cnrsum:
    return(['Aaron',3])
  elif arsum == crsum:
    return(['Aaron',2])
  elif anrsum == cnrsum:
    return(['Aaron',1])
  else:
    success +=1
  erepeating = []
  enonrepeating = set()
  b = a + 1
  while b != 1:
    for i in range(2, b + 1):
      if b % i == 0:
        factors = 0
        for j in range(2, i):
          if i % j == 0:
            factors += 1
        if factors == 0:
          erepeating.append(i)
          enonrepeating.add(i)
          b = int(b/i)
  erepeating.sort()
  ersum = 0
  enrsum = 0
  for i in erepeating:
    ersum += i
  for i in enonrepeating:
    enrsum += i
​
  if arsum == ersum and anrsum == enrsum:
    return(['Ruth',3])
  elif arsum == ersum:
    return(['Ruth',2])
  elif anrsum == enrsum:
    return(['Ruth',1])
  elif success == 1:
    return(1==0)

