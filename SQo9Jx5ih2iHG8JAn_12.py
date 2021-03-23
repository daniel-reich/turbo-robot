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
  list_num = [int(i) for i in list(str(num))]
  mult_list_num = []
  index = 0  
  for i in list_num:
    mult_list_num.append(i*10**((len(list_num)-1-index)))
    index = index +1
  return ' + '.join( [str(i) for i in [i for i in mult_list_num if i != 0]] )

