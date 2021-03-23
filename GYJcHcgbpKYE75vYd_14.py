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
  num = str(num)
  if num.endswith('0') or num.endswith('4') or num.endswith('5') or num.endswith('6') or num.endswith('7') or num.endswith('8') or num.endswith('9'):
    return num + '-TH'
  else:
    if num.endswith('1'):
      if num.endswith('11'):
        return num + '-TH'
      return num+'-ST'
    if num.endswith('2'):
      if num.endswith('12'):
        return num + '-TH'
      return num+'-ND'
    if num.endswith('13'):
      return num+'-TH'
    return num+'-RD'

