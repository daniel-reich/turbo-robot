"""


This is a **reverse coding challenge**. Normally you're given explicit
directions with how to create a function. Here, you must generate your own
function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the
sample outputs shown.

### Examples

    3 ➞ 21
    
    9 ➞ 2221
    
    17 ➞ 22221
    
    24 ➞ 22228

### Notes

If you get stuck, check the **Comments** for help.

"""

def mystery_func(num):
  prev = 0
  asd = 2
  count = 1
  while True:
    prev = asd
    asd =+ asd * 2
    if asd > num:
      return int((count * '2') + str(num - prev))
    count += 1

