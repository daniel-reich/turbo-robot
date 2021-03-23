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
    if num1 =='' and num2=='':
        return '0'
    if num1=='':
        return num2
    if num2=='':
        return num1
    num1 = list(num1)
    num2 = list(num2)
    for i in num1:
        if i in ('1','2','3','4','5','6','7','8','9','0'):
            num1 = ''.join(num1)
        else:
            return '-1'     
    for i in num2:
        if i in ('1','2','3','4','5','6','7','8','9','0'):
            num2 = ''.join(num2)
        else:
            return '-1'  
        result = int(num1) + int(num2)
        return str(result)

