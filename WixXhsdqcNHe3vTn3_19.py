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

def how_bad(n): 
  c = "{0:b}".format(n).count('1')
  def is_pernicious(n):
    if n==2 or n==3: return ["Pernicious"]
    if n%2==0 or n<2: return []
    for i in range(3, int(n**0.5)+1, 2):   
      if n%i==0:
        return []
    return ["Pernicious"]
  def is_evil(n):
    if n%2==0: return ["Evil"]
    else: return ["Odious"]
  return sorted(is_pernicious(c)+is_evil(c))

