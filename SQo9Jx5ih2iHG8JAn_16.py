"""


Create a function that expands a number into a string as shown below:

    25 ➞ "20 + 5"
    70701 ➞ "70000 + 700 + 1"
    685 ➞ "600 + 80 + 5"

### Examples

    expanded_form(70304) ➞ "70000 + 300 + 4"
    
    expanded_form(1037903) ➞ "1000000 + 30000 + 7000 + 900 + 3"
    
    expanded_form(802539) ➞ "800000 + 2000 + 500 + 30 + 9"

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
      
  num = str(num)
  parts = get_parts(num)
  
  prts = [str(int(num[n]) * int(parts[n])) for n in range(len(num)) if num[n] != '0']
  
  return ' + '.join(prts)

