"""


Create a function that expands a decimal number into a string as shown below:

    25.24 ➞ "20 + 5 + 2/10 + 4/100"
    70701.05 ➞ "70000 + 700 + 1 + 5/100"
    685.27 ➞ "600 + 80 + 5 + 2/10 + 7/100"

### Examples

    expanded_form(87.04) ➞ "80 + 7 + 4/100"
    
    expanded_form(123.025) ➞ "100 + 20 + 3 + 2/100 + 5/1000"
    
    expanded_form(50.270) ➞ "50 + 2/10 + 7/100"

### Notes

N/A

"""

def expanded_form(num):
  def get_parts(number, i=0):
    if i == len(number):
      return []
    else:
      tr = '1'
      while len(tr) < len(number[i:]):
        tr += '0'
      return [tr] + get_parts(number, i+1)
  def get_fractions(number, i=0):
    if i == len(number):
      return []
    else:
      if number[i] == '0':
        return [] + get_fractions(number, i+1)
      return ['{}/{}'.format(number[i], (10 ** (i+1)))] + get_fractions(number, i+1)
  
  num, dec = str(num).split('.')
  parts = get_parts(num)
  fracs = get_fractions(dec)
  
  prts = [str(int(num[n]) * int(parts[n])) for n in range(len(num)) if num[n] != '0'] + fracs
  
  return ' + '.join(prts)

