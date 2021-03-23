"""


Create a function that returns which chapter is **nearest** to the page you're
on. If two chapters are equidistant, return the chapter with the **higher**
page number.

### Examples

    nearest_chapter({
      "Chapter 1" : 1,
      "Chapter 2" : 15,
      "Chapter 3" : 37
    }, 10) ➞ "Chapter 2"
    nearest_chapter({
      "New Beginnings" : 1,
      "Strange Developments" : 62,
      "The End?" : 194,
      "The True Ending" : 460
    }, 200) ➞ "The End?"
    nearest_chapter({
      "Chapter 1a" : 1,
      "Chapter 1b" : 5
    }, 3) ➞ "Chapter 1b"

### Notes

All page numbers in the dictionary will be valid integers.

"""

def nearest_chapter(chapt, page):
    rev_chapt = {v: k for k, v in chapt.items()}
    if page in rev_chapt:
        return rev_chapt[page]
    if page < min(rev_chapt.keys()):
        return "Chapter 1"
    if page > max(rev_chapt.keys()):
        return rev_chapt[max(rev_chapt.keys())]
    low = 0
    for p in sorted(rev_chapt.keys()):
        if p < page:
            low = p
        elif p > page:
            high = p
            break
    return rev_chapt[high] if high - page <= page - low else rev_chapt[low]

