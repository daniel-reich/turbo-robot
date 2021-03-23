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
  if any([l.isalpha() for l in num1]) or any([l.isalpha() for l in num2]): return '-1'
  return str(change_num(num1) + change_num(num2))
 
def change_num(num):
  if num == "" : return 0
  for i,n in enumerate(num):    
    if n != "0":
      num = num[i:]
      break
  return int(num)

