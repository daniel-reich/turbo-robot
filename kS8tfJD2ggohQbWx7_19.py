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
  names_list = []
  for n in names:
    names_list.append(n.split(" "))
  names_sorted = sorted(names_list, key=lambda x:x[1])
  names_sorted = sorted(names_sorted, key=lambda x:len(x[1]))
  names_final = []
  for j in range(0, len(names_sorted)):
    names_final.append(" ".join(names_sorted[j]))
  return names_final

