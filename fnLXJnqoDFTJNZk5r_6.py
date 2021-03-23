"""
Write a sorting function that takes in a list of names and sorts them **by
last name** either alphabetically (`ASC`) or reverse-alphabetically (`DESC`).

### Examples

    sort_contacts([
      "John Locke",
      "Thomas Aquinas",
      "David Hume",
      "Rene Descartes"
    ], "ASC") ➞ [
      "Thomas Aquinas",
      "Rene Descartes",
      "David Hume",
      "John Locke"
    ]
    
    # Aquinas (A) < Descartes (D) < Hume (H) < Locke (L)
    
    sort_contacts([
      "Paul Erdos",
      "Leonhard Euler",
      "Carl Gauss"
    ], "DESC") ➞ [
      "Carl Gauss",
      "Leonhard Euler",
      "Paul Erdos"
    ]
    
    # Gauss (G) > Erdos (ER) > Euler (EU)
    
    sort_contacts([], "DESC") ➞ []
    
    sort_contacts(null, "DESC") ➞ []
    
    sort_contacts(undefined, "DESC") ➞ []

### Notes

  * A list with a single name should be trivially returned.
  * An empty list, or an input of `None` should return an empty list.

"""

def sort_contacts(names, sort):
  if names is None:
    return []
  if len(names) == 1:
    return names
  listNames = []
  for x in names:
    y = x.split(' ')
    listNames.append(y[1])
  if sort == 'ASC':
    reverser = False
  else:
    reverser = True
  listNames.sort(reverse=reverser)
​
  ret = []
​
  for z in listNames:
    for a in names:
      if z in a:
        ret.append(a)
  return ret
#The most okay-est solution I've written.

