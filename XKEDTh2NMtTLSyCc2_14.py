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
  a = str(number)[::-1]
  b = 0
  for i in range(len(a)):
      if i%2==0:
          b += int(a[i])
      else:
          if int(a[i])*2 > 9: b += int(a[i])*2 - 9
          else: b += int(a[i])*2
  return b%10==0

