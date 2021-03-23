"""


Replace the numbers in a string with their binary form.

### Examples

    replace_nums("I have 2 sheep.") ➞ "I have 10 sheep."
    
    replace_nums("My father was born in 1974.10.25.") ➞ "My father was born in 11110110110.1010.11001."
    
    replace_nums("10hell76o4 boi") ➞ "1010hell1001100o100 boi"

### Notes

  * There are possibly two or more numbers in a single word (I do not recommend splitting the text at spaces, it surely won't help).
  * Anything separates two numbers, even spaces ("2 2" --> "10 10").

"""

def replace_nums(txt):
  res = ''
  mini = []
  for i in range(len(txt)):
    item = txt[i]
    if not item.isnumeric() and not ('0' <= txt[i-1] and txt[i-1] <= '9'):
      res += item
    if item.isnumeric():
      mini.append(item)
    if not item.isnumeric() and '0' <= txt[i-1] and txt[i-1] <= '9':
      bn = bin(int(''.join(mini))).replace('0b', '')
      res += bn
      mini = []
      res += item
  return res
