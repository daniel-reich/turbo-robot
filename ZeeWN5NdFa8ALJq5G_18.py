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

def nearest_chapter(d: dict, p: int) -> str:
    keys = sorted(list(d.keys()))
    closest = []
​
    for i, key in enumerate(keys):
        if d[key] < p:
            continue
​
        if i - 1 >= 0:
            closest.append(key)
            closest.append(keys[i - 1])
            break
​
        else:
            return key
​
    a = closest[0]
    b = closest[1]
​
    if abs(p - d[a]) <= abs(p - d[b]):
        return a
​
    return b

