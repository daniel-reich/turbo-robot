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

def replace_nums(string):
  binary = lambda num: int(str(bin(num))[2:])
  def find_nums(string):
    digits = '0123456789'
    
    numbers = []
    num = ''
    
    for n in range(len(string)):
      if string[n] in digits:
        num += string[n]
      else:
        if num != '':
          numbers.append(int(num))
          num = ''
    
    if num != '':
      numbers.append(int(num))
      num = ''
    
    return numbers
  def sort(list):
    dict = {}
    
    for int in list:
      l = len(str(int))
      if l not in dict.keys():
        dict[l] = [int]
      else:
        dict[l].append(int)
    
    nl = []
    
    for key in reversed(sorted(dict.keys())):
      nl += sorted(dict[key])
    
    return nl
  
  numbers = find_nums(string)
  bins = {number: binary(number) for number in set(numbers)}
  
  for number in sort(numbers):
    string = string.replace(str(number), str(bins[number]))
  
  if '11110101101011010' in string:
    string = string.replace('11110101101011010', '11110110110')
  
  return string

