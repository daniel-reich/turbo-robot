"""


A positive number's population is the sum of 1's in its binary representation.

  * An **evil** number has an even numbered population.
  * An **odious** number has an odd numbered population.
  * A number is **pernicious** if its _population_ is a prime number.

Create a function that takes a number as an argument and returns a sorted list
of all its descriptors ("Evil", "Odious", or "Pernicious").

### Examples

    how_bad(7) ➞ ["Odious", "Pernicious"]
    # 7 in binary is "111".
    # 1 + 1 + 1 = 3 in "111" means "Odious" should be added to the list answer.
    # 3 is a prime number, meaning "Pernicious" should also be added.
    
    how_bad(17) ➞ ["Evil", "Pernicious"]
    # 17 in binary is "10001".
    # 1 + 1 = 2 in "10001" means "Evil" should be added to the list answer.
    # 2 is a prime number, meaning "Pernicious" should also be added.
    
    how_bad(23) ➞ ["Evil"]
    # 23 in binary is "10111".
    # Four 1's in "10111" means "Evil" should be added to the list answer.
    # 4 is not a prime number, meaning "Pernicious" should not be added.

### Notes

N/A

"""

import re
def isPrime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
    
def how_bad(n):
  s=''
  while n>0:
    i = n%2
    n=int(n/2)
    s += str(i)
  lst =[]
  t=0
  if len(re.findall('[1]',s)) % 2 ==0:
    lst.append("Evil")
  else: 
    lst.append("Odious")
  for i in enumerate(re.findall('[1]',s)):
    t = t + int(i[1])*(2**int(i[0]))
  if isPrime(t):
    lst.append("Pernicious")
  return lst

