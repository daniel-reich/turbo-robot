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
  a, b = str(n).split('.')
  r = [k + '0'*(len(a)-1-i) for i, k in enumerate(a) if k != '0'] + \
      [k + '/1' + '0'*(i+1) for i, k in enumerate(b) if k != '0']
  return ' + '.join(r)

