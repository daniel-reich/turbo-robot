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
  def name_formatter(names):
    tr = {}
    for name in names:
      first, last = name.split()  
      tr[last] = name
    return tr
  def length_sorter(last_names):
    tr = {}
    for name in last_names:
      if len(name) not in tr.keys():
        tr[len(name)] = [name]
      else:
        tr[len(name)].append(name)
    return tr
  
  nf = name_formatter(names)
  ls = length_sorter(list(nf.keys()))
  
  tr = []
  
  for length in sorted(list(ls.keys())):
    if len(ls[length]) > 1:
      nl = sorted(ls[length])
    else:
      nl = ls[length]
    
    for item in nl:
      tr.append(nf[item])
  
  return tr

