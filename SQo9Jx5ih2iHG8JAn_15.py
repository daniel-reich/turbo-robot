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
  num_arr = [int(e) for e in str(num)]
  
  num_str = ""
  for i, num in enumerate(num_arr):
    if num != 0:
      if i != 0:
        num_str += " + "
      num_str += str(num * (10**(len(num_arr)-1-i)))
      
  return num_str

