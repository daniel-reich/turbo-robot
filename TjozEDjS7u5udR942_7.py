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
  import re
  def ln(name):
    return re.findall(r"\w+",name)[-1].lower()
  return sorted(lst,key=ln)

