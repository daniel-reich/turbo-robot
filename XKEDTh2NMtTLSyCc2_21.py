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
    sayi = list(str(number)[::-1])
    for i in range(1, len(sayi),2):
        sayi[i] = int(sayi[i])*2
        if sayi[i] > 9: sayi[i] -= 9
    total = 0
    for i in sayi[1:]: total += int(i)
    return (total * 9)%10 == int(sayi[0])

