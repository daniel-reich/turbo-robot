"""


Write a function that calculates the **factorial** of a number
**recursively**.

### Examples

    factorial(5) ➞ 120
    
    factorial(3) ➞ 6
    
    factorial(1) ➞ 1
    
    factorial(0) ➞ 1

### Notes

N/A

"""

def factorial(n):
  result = 1
  num = n
  myRange = range(num + 1)
​
  for index, item in enumerate(myRange, start=1):
    lastItem = myRange[len(myRange) - index]
​
    if lastItem == 0:
      pass
    else:
      result *= lastItem
      continue
  
  return result

