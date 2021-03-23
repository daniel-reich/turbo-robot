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
    keys_lis = sorted(list(chapt.keys()))
    mem_pg = [keys_lis[0],chapt[keys_lis[0]]]
    for key in keys_lis: 
        if chapt[key] >= page: 
            if chapt[key] - page<= page - mem_pg[1]: 
                return key
            else: 
                return mem_pg[0]
        mem_pg = [key,chapt[key]]

