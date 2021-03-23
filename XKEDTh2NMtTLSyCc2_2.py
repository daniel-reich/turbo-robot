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
  check, n = int(str(number)[-1]), str(number)[::-1][1:]
  double = [int(x) * 2 if not index % 2 else int(x) for index, x in enumerate(n)]
  plus = sum(int(str(x)[0]) + int(str(x)[1]) if len(str(x)) == 2 else x for x in double)
  return 14 <= len(str(number)) <= 19 and 10 - int(str(plus)[-1]) == check

