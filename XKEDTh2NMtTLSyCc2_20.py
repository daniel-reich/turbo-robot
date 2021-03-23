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
    lst = list(map(int, str(number)))
    a = lst[:]
    a[1::2] = [int(str(x*2)[0]) + int(str(x*2)[1]) if x >= 5 else x*2 for x in a[1::2]]
    lst[::2] = [int(str(x*2)[0]) + int(str(x*2)[1]) if x >= 5 else x*2 for x in lst[::2]]
    
    return not sum(lst) % 10 or not sum(a) % 10

