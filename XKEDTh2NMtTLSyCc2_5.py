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
    total = 0
    digits = [int(i) for i in str(n)[::-1]]
    check = digits.pop(0)
​
    for idx, i in enumerate(digits):
        if idx%2:
            total += i
        else:
            total += i*2 if i < 5 else i*2 - 9
    return (9*total)%10 == check

