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

def add_str_nums(n1, n2):
  final = []
  for n in n1,n2:
    if n == "":
      final.append(0)
    else:
      try:
        final.append(int(n))
      except:
        return "-1"
  return str(sum(final))

