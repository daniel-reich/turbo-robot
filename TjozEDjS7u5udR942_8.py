"""


Create a function which sorts a list of authors **by their last name**. The
list may include initials and fullnames, but note that there will be a **mix**
of upper and lowercase.

### Examples

    sort_authors(["J. K. Rowling", "w. s.", "lewis carroll", "M. M."]) ➞ ["lewis carroll", "M. M.", "J. K. Rowling", "w. s."]
    
    sort_authors(["J. L.", "J. B. priestley", "L. C.", "Suzanne Collins"]) ➞ ["L. C.", "Suzanne Collins", "J. L.", "J. B. priestley"]

### Notes

  * If two surnames begin with the same letter, return them in the order they appeared.
  * Note how there are spaces between each of the initials.

"""

def sort_authors(lst):
  lst2 = []
  for i in range(0, len(lst)):
    x = lst[i].split(" ")
    lst2.append(x[-1].upper() + str(i))
  lst2 = sorted(lst2)
  for i in range(0, len(lst2)):
    lst2[i] = lst2[i][-1]
  lst3 = []
  for i in range(0, len(lst)):
    lst3.append(lst[int(lst2[i])])
  return lst3

