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
  num=str(num)[::-1]
  ans=[]
  for i in range(len(num)):
    if num[i]!='0':ans.append(num[i]+'0'*i)
  return ' + '.join(ans[::-1])

