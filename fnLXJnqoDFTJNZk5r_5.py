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
  if not names:
    return []
  l2 = [Z.split() for Z in names]
  if sort == 'ASC':
    l3 = sorted(l2, key=lambda x: x[1])
  else:
    l3 = sorted(l2, key=lambda x: x[1], reverse=True)
  return [' '.join(Z) for Z in l3 ]
