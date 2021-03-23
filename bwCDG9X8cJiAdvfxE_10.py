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
    n1 = [i for i in num1]
    n2 = [i for i in num2]
    c = 0
    if len(n1)!=0:
        for i in n1:
            if ord(i)<48 or ord(i)>57:
                c = 1
                break
            else:
                pass
    else:
        n1 = ["0"]
    
    if len(n2)!=0:
        for i in n1:
            if ord(i)<48 or ord(i)>57:
                c = 1
                break
            else:
                pass
    else:
        n2 = ["0"]
    if c!= 1: 
        return str(int("".join(n1)) + int("".join(n2)))
    else:
        return "-1"

