"""


Create a function that takes an integer and returns it as an **ordinal
number**. An Ordinal Number is a number that tells the position of something
in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.

### Examples

    return_end_of_number(553) ➞ "553-RD"
    
    return_end_of_number(34) ➞ "34-TH"
    
    return_end_of_number(1231) ➞ "1231-ST"
    
    return_end_of_number(22) ➞ "22-ND"
    
    return_end_of_number(412) ➞ "412-TH"

### Notes

Check the **Resources** tab for more info on _ordinal numbers_.

"""

def return_end_of_number(num):
  if num == 1 or num % 100 > 20 and num % 10 == 1:
    return '{}-ST'.format(num)
  if num == 2 or num % 100 > 20 and num % 10 == 2:
    return '{}-ND'.format(num)
  if num == 3 or num % 100 > 20 and num % 10 == 3:
    return '{}-RD'.format(num)
  return '{}-TH'.format(num)

