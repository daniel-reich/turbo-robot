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
  a, b = str(num).split('.')
  lst1 = [x + '0' * (len(a) - i - 1) for i, x in enumerate(a) if x != '0']
  lst2 = ["{}/1{}".format(x, '0' * (i + 1)) for i, x in enumerate(b) if x != '0']
  return ' + '.join(lst1 + lst2)

