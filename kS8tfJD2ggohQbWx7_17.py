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
  lst = []
  for i in names:
    if len(lst) == 0:
      lst.append(i)
    else:
      lst = sort(i, lst)
  return lst
​
def sort(name, lst):
  lastname = get_lastname(name)
  for i in range(len(lst)):
    compare_lastname = get_lastname(lst[i])
    if len(lastname) < len(compare_lastname):
      lst.insert(i, name)
      break
    elif len(lastname) == len(compare_lastname):
      if ord(lastname[0]) <  ord(compare_lastname[0]):
        lst.insert(i, name)
      else:
        lst.insert(i+1, name)
      break
    elif i == len(lst)-1:
      lst.insert(i, name)
      break
  return lst
      
def get_lastname(name):
  index_space = name.find(" ")
  lastName = name[index_space+1:]
  return lastName

