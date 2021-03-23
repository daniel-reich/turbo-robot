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
    a = [int(i) for i in str(number)[::-1]]
    for digit in range(1,len(a)):
        if digit % 2 != 0:
            a[digit] = a[digit] * 2
            if a[digit] > 9:
                a[digit] -= 9
    if 9*(sum(a[:-1])) % 10 == a[-1]:
        return True
    return False

