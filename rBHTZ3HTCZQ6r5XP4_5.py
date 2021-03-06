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

def expanded_form(n):
  a,b = str(n).split('.')
  a = ' + '.join([str((10**(len(a)-i-1))*int(j)) for i,j in enumerate(a) if str((10**(len(a)-i-1))*int(j))!='0'])
  b = ' + '.join([str(int(j))+'/'+str('1'+'0'*(i+1)) for i,j in enumerate(b) if str(int(j))!='0'])
  return a +' + ' + b if a and b else b if not a else a

