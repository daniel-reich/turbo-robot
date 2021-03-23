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
  names =[i.split() for i in names]
  d = {i[1]:i[0] for i in names}
  last = sorted(sorted(d.keys()),key=len)
  return [d.get(i) + ' ' + i for i in last]

