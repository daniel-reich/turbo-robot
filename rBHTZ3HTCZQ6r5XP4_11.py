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
  o = str(num)[:str(num).index('.')]
  d = str(num)[str(num).index('.') + 1:]
  s = []
​
  for i in range(len(o)):
    if o[i] != '0':
      s.append(str(int(o[i]) * 10 ** (len(o) - i - 1)))
​
  for i in range(len(d)):
    if d[i] != '0':
      s.append(str(d[i]) + '/' + str(10 ** (i+1)))    
​
  return ' + '.join(s)

