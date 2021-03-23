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
  numbers = []
  sum_numbers = 1
  while sum_numbers <= num:
    numbers.append(2)
    sum_numbers = sum_numbers * 2
    
  sum_numbers = sum_numbers / 2
  numbers = numbers[1:]
  numbers.append(int(num - sum_numbers))
  
  result = ""
  for i in numbers:
    result = result + str(i)
  
  return int(result)

