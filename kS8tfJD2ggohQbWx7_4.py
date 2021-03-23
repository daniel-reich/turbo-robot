"""


Create a function that takes a list of names in the format "First Name Last
Name" (e.g. "John Doe"), and returns a list of these names sorted by the
**length** of their **last** names. If the length of multiple last names are
the same, then proceed to sort alphabetically by last name.

### Examples

    last_name_lensort([
      "Jennifer Figueroa",
      "Heather Mcgee",
      "Amanda Schwartz",
      "Nicole Yoder",
      "Melissa Hoffman"
    ]) ➞ ["Heather Mcgee", "Nicole Yoder", "Melissa Hoffman", "Jennifer Figueroa", "Amanda Schwartz"]

### Notes

If last names are of the same length, sort alphabetically by last name.

"""

def last_name_lensort(names):
  
  Surnames = []
  
  Counter = 0
  Length = len(names)
  
  while (Counter < Length):
    Full = names[Counter]
    Blocks = Full.split(" ")
    Surnames.append(Blocks[1])
    Counter += 1
  
  Surnames = sorted(Surnames, key = lambda x : (len(x), x))
  
  Revised = []
  
  Taken = 0
  
  NC = 0
  NL = len(names)
​
  SC = 0
  SL = len(Surnames)
  
  while (NC < NL) and (SC < SL):
    Wanted = Surnames[SC]
    Checking = names[NC]
    
    if (Wanted in Checking):
      Revised.append(Checking)
      SC += 1
      NC = 0
    else:
      NC += 1
  
  return Revised

