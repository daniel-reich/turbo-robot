"""


Write a function that adds two numbers. The catch, however, is that the
numbers will be strings.

### Examples

    add_str_nums("4", "5") ➞ "9"
    
    add_str_nums("abcdefg", "3") ➞ "-1"
    
    add_str_nums("1", "") ➞ "1"
    
    add_str_nums("1874682736267235927359283579235789257", "32652983572985729") ➞ "1874682736267235927391936562808774986"

### Notes

  * If there are any non-numerical characters, return `"-1"`.
  * An empty parameter should be treated as `"0"`.
  * Python supports the addition of integers without limit, try this challenge without using this functionality.
  * Your function doesn't have to add negative numbers.
  * Zeros at the beginning of the string should be trimmed.

"""

def add_str_nums(num1, num2):
​
  # Bucket for Grand Total
  Total = 0
  
  # Converting num1 to List
  List_A = list(num1)
  
  # Adding Up Value of List_A (aka num1)
  Multiple = 1
  
  Cursor = -1
  Length = len(List_A)
  End = Length * -1
  
  while (Cursor >= End):
    Item = List_A[Cursor]
    
    if (Item.isdigit()):
      Digit = int(Item)
      Value = Digit * Multiple
      Total += Value
      Multiple *= 10
      Cursor -= 1
    else:
      return "-1"
  
  # Converting num2 to List
  List_B = list(num2)
  
  # Adding Up Value of List_B (aka num2)
  Multiple = 1
  
  Cursor = -1
  Length = len(List_B)
  End = Length * -1
  
  while (Cursor >= End):
    Item = List_B[Cursor]
    
    if (Item.isdigit()):
      Digit = int(Item)
      Value = Digit * Multiple
      Total += Value
      Multiple *= 10
      Cursor -= 1
    else:
      return "-1"
  
  # Giving Answer (if all were digits)
  return str(Total)

