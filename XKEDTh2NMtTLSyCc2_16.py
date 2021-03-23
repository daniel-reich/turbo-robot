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
  if len(str(number)) == 16:
    y = [int(char) for char in str(number)[::-1]]
    for i in range(16):
      if i%2:
        y[i] = y[i]*2
      if y[i] > 9:
        y[i] = y[i] - 9
    if not sum(y)%10:
      return True
    else:
      return False
  else:
    return True

