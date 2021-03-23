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
    lst2 = [(i.split()[-1][0]) for i in lst ]
    lst3 = sorted([(i[0].lower(),j) for j,i in enumerate(lst2)])
    return [lst[i[1]] for i in lst3]

