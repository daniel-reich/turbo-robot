"""


Create a function that takes a number and checks whethers the given number is
a valid credit card number using **Luhn Algorithm**. The return value is
boolean.

### Examples

    valid_credit_card(4111111111111111) ➞ True
    # Visa Card
    
    valid_credit_card(6451623895684318) ➞ False
    # Not a valid credit card number.
    
    valid_credit_card(6451623895684318) ➞ False

### Notes

  * American Express/VISA/Discover/Diner Club may be the credit card type.
  * Check the **Resources** for help.

"""

def valid_credit_card(number):
  list1 = []
  summ = 0
  for i in str(number):
    list1.insert(0, i)
  for n, i in enumerate(list1):
    if (n + 1) % 2 == 0:
      list1[n] = str(int(i) * 2)
    if int(list1[n]) > 9:
      list1[n] = str(int((list1[n])[0]) + int((list1[n])[1]))
    summ += int(list1[n])
  return summ % 10 == 0

