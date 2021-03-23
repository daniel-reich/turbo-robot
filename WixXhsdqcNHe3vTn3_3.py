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
  hbad = []
  binary = '{0:0b}'.format(n)
  if binary.count('1') % 2 == 0:
    hbad.append('Evil') 
  elif binary.count('1') % 2 != 0:
    hbad.append('Odious')
  if binary.count("1") > 1:
    if binary.count("1") == 2:
      hbad.append('Pernicious')
    else:
      for i in range(2, binary.count("1")):
        if binary.count("1") % i == 0:
          break
        else:
          if 'Pernicious' not in hbad:
            hbad.append('Pernicious')
          else:
            break
  return hbad

