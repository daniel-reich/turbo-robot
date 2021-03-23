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
    import operator
    ans = {idx: (i.strip('.').split(' ')[-1][0].lower()) for idx, i in enumerate(lst)}
    ans = sorted(ans.items (), key=operator.itemgetter (1))
    return [lst[(i[0])] for i in ans]

