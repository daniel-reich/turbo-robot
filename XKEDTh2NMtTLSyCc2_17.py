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
  num = [int(i) for i in str(number)]
  numrev = num[-2: -17: -1]
  mult = [i[1]*2 if i[0] % 2 == 0 else i[1] for i in enumerate(numrev)]
  remove = [i - 9 if i >= 9 else i for i in mult]
  return (sum(remove) + num[len(num) - 1]) % 10 == 0

