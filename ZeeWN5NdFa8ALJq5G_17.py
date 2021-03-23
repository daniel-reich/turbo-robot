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

from statistics import mean
def nearest_chapter(chapt, page):
  nums = sorted(chapt.values())
  chaps = sorted(chapt.keys(),key = lambda x: chapt[x])
  for i,chap in enumerate(nums):
    try:
      if page <= chap:
        avg = mean([nums[i-1],chap])
        return chaps[i] if page >= avg else chaps[i-1]
    except IndexError:
      if page <= nums[0]:
        return chaps[0]
  return chaps[-1]

