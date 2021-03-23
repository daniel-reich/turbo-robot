"""


Create a function that takes an integer and returns it as an **ordinal
number**. An Ordinal Number is a number that tells the position of something
in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.

### Examples

    return_end_of_number(553) ➞ "553-RD"
    
    return_end_of_number(34) ➞ "34-TH"
    
    return_end_of_number(1231) ➞ "1231-ST"
    
    return_end_of_number(22) ➞ "22-ND"
    
    return_end_of_number(412) ➞ "412-TH"

### Notes

Check the **Resources** tab for more info on _ordinal numbers_.

"""

def return_end_of_number(num):
  teen = ['11', '12', '13']
  ords = {1: 'ST', 2: 'ND', 3: 'RD'}
  rem = num % 10
  numeral = str(num)
  end = '-'
  if numeral[-2:] in teen:
    end += 'TH'
  elif rem in ords:
    end += ords[rem]
  else:
    end += 'TH'
  return '{}{}'.format(numeral, end)

