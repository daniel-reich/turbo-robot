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

from operator import itemgetter
def sort_authors(lst):
  temp = [" ".join(itm) for itm in sorted([itm.lower().split() for itm in lst], key=itemgetter(-1))]
  res = [temp.index(itm.lower()) for itm in lst]
  return [lst[i] for i in res]

