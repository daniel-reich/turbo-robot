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

def expanded_form(num: float) -> str:
  gt1, lt1 = str(num).split('.')
  result = []
  for i in range(len(gt1)):
    if gt1[i] != '0':
      result.append(gt1[i] + '0' * (len(gt1) - 1 - i))
  for i in range(len(lt1)):
    if lt1[i] != '0':
      result.append(lt1[i] + '/1' + '0' * (i + 1))
  return ' + '.join(result)

