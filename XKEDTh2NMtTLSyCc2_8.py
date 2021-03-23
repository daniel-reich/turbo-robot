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

def valid_credit_card(n):
  lst = [2 * int(i) if n % 2 == 0 else int(i) 
          for n, i in enumerate(str(n)[:-1][::-1])]
  lst = [i if i <= 9 else i-9 for i in lst][::-1]
  x = (sum(lst) * 9) % 10
  return str(n)[:-1] + str(x) == str(n)

